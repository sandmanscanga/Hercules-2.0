"""Module for running the threader"""
import threading
import queue


class Threader:
    """Class to handle the threading"""

    STOP_SIGNAL = False
    CURRENT = 0

    def __init__(self, total_threads, attack_function, result_function):
        self.total_threads = total_threads
        self.attack_function = attack_function
        self.result_function = result_function
        self.semaphore = threading.Lock()
        self.que = queue.Queue()
        self.threads = None

    def start_threads(self):
        """Starts all of the threads in the staging loop"""

        self.threads = []
        for index in range(self.total_threads):
            child_id = index + 1
            thread = threading.Thread(
                target=self._stager,
                args=(child_id, self),
                daemon=True
            )
            thread.start()
            self.threads.append(thread)

    def add_job(self, job):
        """Adds a job to the queue for the threads to run"""

        self.que.put(job)

    def join_threads(self):
        """Applies natural kill signals and waits until finished"""

        for _ in range(self.total_threads):
           self.que.put(None)  # sends local kill signal

        clean_exit = True
        for thread in self.threads:
            try:
                thread.join()
            except KeyboardInterrupt:
                clean_exit = False
                break

        return clean_exit

    @staticmethod
    def _stager(child_id, instance):
        """Slave loop for threads"""

        while True:
            if Threader.STOP_SIGNAL is True:
                break  # received global kill signal

            data = instance.que.get()  # blocking call
            if data is None:
                break  # received local kill signal

            result = instance.attack_function(data)
            if result:
                with instance.semaphore:
                    Threader.CURRENT += 1
                    args = (data, result, child_id, Threader.CURRENT)
                    finish = instance.result_function(args)
                    if finish is True:
                        Threader.STOP_SIGNAL = True  # send global kill signal
            else:
                with instance.semaphore:
                    if Threader.STOP_SIGNAL is False:
                        Threader.CURRENT += 1
                        args = (data, result, child_id, Threader.CURRENT)
                        _ = instance.result_function(args)

            instance.que.task_done()
