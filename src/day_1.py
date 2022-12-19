if __name__ == "__main__":

    all_elfs = []

    with open("input/day_1.txt", "r") as input:
        for line in input:
            all_elfs.append(line.strip().split(","))

    all_elfs_int = [[int(calory) for calory in elf_bag] for elf_bag in all_elfs]

    all_elfs_sum = [sum(elf_bag) for elf_bag in all_elfs_int]

    print(f"part 1 answer: {max(all_elfs_sum)}")

    all_elfs_sum.sort(reverse=True)

    print(f"part 2 answer {sum(all_elfs_sum[0:3])}")
