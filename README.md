# UnstableUtilities
![Build Status](https://github.com/software-students-fall2024/3-python-package-this-package/actions/workflows/python-package.yml/badge.svg)


## Description

UnstableUtilities is an almost useless Python package. It provides several tools to make your life a bit easier, or a lot harder: a calculator, a current date generator, a countdown timer, a message encoder, and a decoder. Each tool is unstable; it might give you the correct result, an incorrect result, or even shut down your computer!

__IMPORTANT:__ Save all progress on your computer before using this package! Always use with caution. Even better, avoid using it unless you are completely clear on what each function does. If a system shutdown is ever triggered, terminate the current program IMMEDIATELY to avoid the shutdown unless it is what you want, because every system shutdown function used in this package uses [this unusual timer function](#3-start-a-countdown-timer) to perform a 20-second countdown. A convenient way to terminate your program is pressing Ctrl-C if you are running your program in the terminal. On MacOS, shutdown will not be successful unless you enter your user password. On Windows, shutdown will be performed immediately after the countdown. 

## PyPi Page

[PyPi](https://pypi.org/project/UnstableUtilities/)

## Team
- [Ziqiu (Edison) Wang](https://github.com/ziqiu-wang)
- [Thomas Chen](https://github.com/ThomasChen0717)
- [An Hai](https://github.com/AnHaii)
- [Annabella Lee](https://github.com/annabellalee0113)


## Installation

__Prerequisite__: Install pip in local environment. We recommend running under virtual environment (see part __How To Test/Run__)<br>


1. install package
    ```
   pip install unstableutilities
   ```


2. import functions
    ```
    from utilities import start_timer
    from utilities import get_date
    from utilities import calculator
    from utilities import decode
    from utilities import encode
    ```

## Usage Examples

Here are the examples in a py file:
[Example.py](https://github.com/software-students-fall2024/3-python-package-this-package/blob/main/example.py)

### 1. Simple Calculator

This package provides a calculator that calculates mathematical expressions with addition, subtraction, multiplication, and division. 

```
calculator(expression: str) -> None
```

This function finds the result of an expression given as a string. It randomly decides whether to perform a correct calculation or an intentionally wrong calculation. With 1% probability, the function will trigger a system shutdown. If the shutdown is not triggered, the function calculates either a correct result with 30% probability or an incorrect result with 70% probability. The function returns ```None``` and prints the calculated result.

The input expression must be a string with space-separated integers and operators. 

Examples: 

- ```calculator(“3 + 6 * 8”)``` is the correct format to use.

- ```calculator(“3 +”)``` is the wrong format to use. The equation should not start or end with an operator.

- ```calculator(“3+6*8”)``` is the wrong format to use. The equation should have spaces between all numbers and operators.

- ```calculator(3 + 6 * 8)``` is the wrong format to use. The function only takes strings. 


### 2. Get Today's Date

This package provides a function that returns today's date as a string.

```
get_date() -> str
```

This function aims to return the current date. There is a 1% chance that a system shutdown will be triggered upon calling the function. If the shutdown is not triggered, there is a 30% chance that the function will return the correct date and a 70% chance that it will return an incorrect date. Among the incorrect results, the function might return a date that exists but is incorrect, a completely absurd date that doesn't exist, or a meaningless code snippet. Each of these three cases has an equal chance of occurring (33.3%).


Examples of possible outputs and their probabilities:

```
get_date() -> 2024-11-04  # Correct date: 28.5%

get_date() -> 2000-12-21  # A possible but incorrect date: 22.2%

get_date() -> 6666-40-59  # A completely absurd date: 22.2%

get_date() -> "if x > 10:\n print('x is large')"  # A generated code snippet: 22.2%

get_date() -> 'system shutdown'  # Shutdown is triggered: 1% 
```

### 3. Start a Countdown Timer

This package provides a countdown timer.

```
start_timer(countdown_time: int = 20) -> None
```

This function takes an optional integer ```countdown_time``` as the only argument, which specifies the number of seconds of the countdown. Default value is 20.

The function simulates a countdown timer and does not return anything. There is a 70% chance that the countdown will proceed normally, decreasing by 1 second every second. If it does not proceed normally, the countdown will switch randomly to one of the following modes each time the nominal remaining time decreases by 1 second:

- normal: Normal countdown, decreasing the nominal remaining time by 1 second every second. 30% probability.

- three_sec_jump: Decreasing the nominal remaining time by 1 second every 3 seconds. 30% probability.

- three_jumps_per_sec: Decreasing the nominal remaining time by 3 seconds every second. 30% probability.

- early_stop: This mode stops the countdown immediately. 10% probability.

The function prints "Done!" after completing the countdown.

__IMPORTANT__: every system shutdown function used in this package uses this timer function to perform a 20-second countdown. Therefore, IMMEDIATELY terminate your program to avoid the shutdown unless it is what you want. A convenient way to terminate your program is using Ctrl-C in the terminal.


### 4. Encoding and Decoding Strings
This package provides four algorithms to encode and decode strings: Morse Code, Caesar, Vigenère, and Base64.


#### Encoding
The encoding function takes as arguments an input string to encode, the type of algorithm to use, and an optional shift (for Caesar) and keyword (for Vigenère).


```
encode(inp_str: str, type: str, shift: int = 1, keyword : str = "key") -> Optional[str]
```


Calling this function has a 1% chance to immediately trigger a system shutdown. If the shutdown is not triggered, it either returns a correctly encoded string with 50% probability or a wrong output with 50% probability. This wrong output is a string that results from applying a random encoding algorithm to each character of the input string.


The function returns ```None``` if the format of any argument is invalid. The format specifications are as follows:


- ```inp_str```: the string that needs to be encoded.
   - For Morse Code algorithm, the string may only contain English letters, digits, or spaces.
   - For Base64, Caesar, and Vigenère algorithms, the string may be any string.


- ```type```: a string that specifies the type of algorithm to use: "morse", "base64", "caesar", or "vigenere". This argument is case-insensitive.


- ```shift```: an integer that indicates the shift used by Caesar algorithm. Must be provided when using Caesar. Default value is 1.


- ```keyword```: a string that specifies the keyword used by Vigenère algorithm. It may only contain English letters. Must be provided when using Vigenère. Default value is "key".


Usage examples for ```encode()```:


```
from crypto import encode

print(encode("input string", type="caesar", shift=3))
print(encode("Input string", type="Vigenere", keyword="key"))
print(encode("Input string1", type="MORSE CODE"))
print(encode("input string", type="base64"))
```


#### Decoding


Just like the encoding function, the decoding function takes as arguments an input string to decode, the type of algorithm to use, and an optional shift (for Caesar) and keyword (for Vigenère).


```
decode(inp_str: str, type: str, shift: int = 1, keyword : str = "key") -> Optional[str]
```


Calling this function has a 1% chance to immediately trigger a system shutdown. If the shutdown is not triggered, it either returns a correctly decoded string with 50% probability or a wrong output with 50% probability. This wrong output can be either a randomly generated string (50% probability), or a string that results from applying a random decoding algorithm to each group of 1-5 characters of the input string (50% probability).


The function returns ```None``` if the format of any argument is invalid. The format specifications are as follows:


- ```inp_str```: the string that needs to be decoded.
   - For Morse Code algorithm, the string may only contain "-", ".", or spaces.
   - For Base64 algorithm, the string may only contain English letters, digits, "+", "/", or "=".
   - For Caesar and Vigenère algorithms, the string may be any string.


- ```type```: a string that specifies the type of algorithm to use: "morse", "base64", "caesar", or "vigenere". This argument is case-insensitive.


- ```shift```: an integer that indicates the shift used by Caesar algorithm when the input string was encoded. Must be provided when using Caesar. Default value is 1.


- ```keyword```: a string that specifies the keyword used by Vigenère algorithm when the input string was encoded. It may only contain English letters. Must be provided when using Vigenère. Default value is "key".


Usage examples for ```decode()```:


```
from crypto import decode

print(decode("input string", type="caesar", shift=3))
print(decode("Input string1", type="Vigenere", keyword="key"))
print(decode(".- -..", type="MORSE CODE"))
print(decode("aGVsbG8=", type="base64"))
```


## How To Test/Run
1. Install pipenv (Suppose you have python. If not, download python first)
    ```
    pip install pipenv
    ```


2. Install Project Dependencies with Pipenv
    ```
    pipenv install --dev
    ```


3. Run Virtual Environment
    ```
    pipenv shell
    ```
4. Enter Editor Mode
    ```
    pip install -e .
    ```

5. Run pytest/python files
    ```
    pytest
    python <filename>.py
    ```




## Contributing
1. Fork the Repository:
- [Our Package](https://github.com/software-students-fall2024/3-python-package-this-package)
- Open our package and click "fork" to save files in your own repository


2. Clone the Repository:<br>
In your own repository, use<br>
    ```
    git clone <repository-url>
    ```


3. Navigate into the Project Directory<br>
    ```
    cd <project-repo>
    ```


4. Create a New Branch for Your Changes:<br>
    ``` 
    git checkout -b feature/my-new-feature
    ```


5. Install Dependencies<br>
    see __How To Test/Run__


6. Make Changes or Add Features


7. Stage Your Changes<br>
    ```
    git add <file-name>
    ```


8. Commit Your Changes<br>
    ```
    git commit -m "your commit"
    ```


9. Push Your Branch to Your Fork<br>
    ```
    git push origin feature/my-new-feature
    ```


10. Create a Pull Request <br>
In the PR, describe the changes you made and their purpose




