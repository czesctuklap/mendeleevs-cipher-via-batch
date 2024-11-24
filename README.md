# Mendeleev's Cipher via batch
Extended version of mendeleevs-cipher project that includes calling program from shell, an html raport and a menu;

The task was to write a program that will encrypt a given text in such a way that, instead of letters, the program will output the atomic number of the element which chemical symbol corresponds to the encrypted letters, ignoring their case. The space between letters should be replaced with an asterisk (*), and the space between words should be replaced with two asterisks (**).

### User Manual
The program is a console application.

After launching through `projekt.bat` file, the user is prompted to choose one of 3 options by entering the corresponding number and confirming with the ENTER key:
1. **Run project** - Encrypting data from the `input.txt` file starts, saving it to the `output.txt` file and as a backup. Then, the user is prompted to choose how they want to display the encrypted data: as console output or as an HTML file.
2. **Information and user guide** - The user will be directed to a detailed instruction and rules regarding entering data. The program also specifies how the word will be encrypted.
3. **Exit** - This option shuts down the program.

The program retrieves data from the `input.txt` file and saves it to the `output.txt` file. It utilizes a `while` loop, iterating from index 0 to the length of the text entered by the user. Then, it employs `if`, `elif`, and `else` statements, along with `for` loops, to analyze the input text and take appropriate steps to encrypt the text or throw an exception if it's not possible. Additionally, a function is created to check if the text can be encrypted, utilizing try and except statements to handle exceptions and output corresponding solutions.

### Program Structure
![structure](https://github.com/czesctuklap/mendeleevs-cipher-via-batch/assets/164773624/716d7c91-4e5f-4a74-84ae-d357071d985f)
