from src.util import rsa
import concurrent.futures


def launch_multi_thread_generate(num_keys, num_thread, nBits):
    thread = []
    keys = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_thread) as executor:
        for _ in range(num_keys):
            thread.append(executor.submit(rsa.generate, nBits))

        for result in concurrent.futures.as_completed(thread):
            keys.append(result.result())
    print("done")