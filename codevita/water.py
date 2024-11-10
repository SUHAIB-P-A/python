import math


def find_peaks(data):
    
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return peaks


def find_widest_valley(data):
    
    peaks = find_peaks(data)
    widest_valley_width = -math.inf
    widest_valley_index = -1

    for i in range(len(peaks) - 1):
        current_valley_width = peaks[i + 1] - peaks[i]
        if current_valley_width > widest_valley_width:
            widest_valley_width = current_valley_width
            widest_valley_index = i

    return widest_valley_width, widest_valley_index + 1


def main():
    # Read input
    n = int(input())
    data = list(map(float, input().split()))

    # Find widest valley
    widest_valley_width, valley_index = find_widest_valley(data)

    # Print output
    print(f"Widest valley width: {widest_valley_width:.4f}")
    print(f"Valley index: {valley_index}")


if __name__ == "__main__":
    main()
