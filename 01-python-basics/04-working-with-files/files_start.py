#
# Read and write files using the built-in Python file methods
#

def main():
    # Open a file for writing and create it if it doesn't exist
    with open("textfile.txt", "w") as f:
        # write some lines of data to the file
        for i in range(10):
            f.write(f"This is another line {i}.\n")
    # close the file when done
    # using a with block closes automatically

    # Open the file for appending text to the end
    with open("textfile.txt", "a") as a:
        for i in range(11, 21):
            a.write(f"I'm now adding this line: {i}.\n")

    # Open the file back up and read the contents
    with open("textfile.txt", "r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
