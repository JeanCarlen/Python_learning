import time
import os


# my own tqdm, a function that display a progress bar using a range
def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_t = time.time()
    terminal_size = os.get_terminal_size().columns - 1
    other_info = (
        f"{100:.0%}|{total}/{total} "
        f"[{59:02d}:{59:02d}<{59:02d}:{59:02d}, {999.99:.2f}it/s]"
    )
    info_len = len(other_info)
    bar_len = terminal_size - info_len

    for i, elem in enumerate(lst, start=1):
        time.sleep(0.001)  # Add a small delay
        progress = i / total
        elapsed = time.time() - start_t
        speed = i / elapsed if elapsed > 0 else 0
        eta = (total - i) / speed if speed > 0 else 0

        completed = int(bar_len * progress)
        bar = '█' * completed + ' ' * (bar_len - completed)

        elapsed_min, elapsed_sec = divmod(int(elapsed), 60)
        eta_min, eta_sec = divmod(int(eta), 60)
        print(
            f"\r{progress:.0%}|{bar}| {i}/{total} "
            f"[{elapsed_min:02d}:{elapsed_sec:02d}"
            f"<{eta_min:02d}:{eta_sec:02d}, {speed:.2f}it/s]",
            end='', flush=True
        )
        yield elem


def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()
