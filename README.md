# Python Package Exercise
![Build Status](https://github.com/software-students-fall2024/3-python-package-this-package/actions/workflows/python-package.yml/badge.svg)


## Description


## PyPi Page


## Team
- [Ziqiu (Edison) Wang](https://github.com/ziqiu-wang)
- [Thomas Chen](https://github.com/ThomasChen0717)
- [An Hai](https://github.com/AnHaii)
- [Annabella Lee](https://github.com/annabellalee0113)


## Installation

- Prerequisite: Installed pip in local environment, recommend running under virtual environment (see part __Install Dependencies and Virtual Environment__)<br>


- Step 1: install package
   <br> ```pip install unstable_utilities```<br>


- Step 2: import package
    <br>```import unstable_utilities```<br>


- Step 3: import function
    <br> ```pip install unstable_utilities```<br>
    

## Usage Examples
### 1. Simple Calculator

This package provides a calculator that calculates mathematical expressions with addition, subtraction, multiplication, and division. 

```calculator(expression: str) -> Union[float, int]```

This function finds the result of an expression given as a string. It randomly decides whether to perform a correct calculation or an intentionally wrong calculation. With 5% probability, the function will trigger a system shutdown. If the shutdown is not triggered, the function returns either a correct result with 30% probability or an incorrect result with 70% probability.

The input expression must be a string with space-separated integers and operators. 

Examples: 

```calculator(“3 + 6 * 8”)``` is the correct format to use.

```calculator(“3 +”)``` is the wrong format to use. The equation should not start or end with an operator.

```calculator(“3+6*8”)``` is the wrong format to use. The equation should have spaces between all numbers and operators.

```calculator(3 + 6 * 8)``` is the wrong format to use. The function only takes strings. 


### 2. Get Today's Date

This package provides a function that returns today's date as a string.

```get_date() -> str```

This function aims to return the current date. There is a 5% chance that a system shutdown will be triggered upon calling the function. If the shutdown is not triggered, there is a 30% chance that the function will return the correct date and a 70% chance that it will return an incorrect date. Among the incorrect results, the function might return a date that exists but is incorrect, a completely absurd date that doesn't exist, or a meaningless code snippet. Each of these three cases has an equal chance of occurring (33.3%).


Examples of possible outputs and their probabilities:

```get_date() -> 2024/11/4``` (correct date): 28.5%

```get_date() -> 2000/12/21``` (an existing but incorrect date): 22.2%

```get_date() -> 6666/40/59``` (a completely absurd date): 22.2%

```get_date() -> "if x > 10:\n print('x is large')"``` (a generated code snippet): 22.2%

```get_date() -> 'system shutdown'``` (shutdown is triggered): 5% 

### 3. Start a Countdown Timer

This package provides a countdown timer.

```timer(countdown_time: int = 20) -> None```

This function takes an optional integer ```countdown_time``` as the only argument, which specifies the number of seconds of the countdown. Default value is 20.

The function simulates a countdown timer and does not return anything. There is a 70% chance that the countdown will proceed normally, decreasing by 1 second every second. If it does not proceed normally, the countdown will switch randomly to one of the following modes each time the nominal remaining time decreases by 1 second:

- normal: Normal countdown, decreasing the nominal remaining time by 1 second every second. 30% probability.

- three_sec_jump: Decreasing the nominal remaining time by 1 second every 3 seconds. 30% probability.

- three_jumps_per_sec: Decreasing the nominal remaining time by 3 seconds every second. 30% probability.

- early_stop: This mode stops the countdown immediately. 10% probability.

The function prints "Done!" after completing the countdown.


### 4. Encoding and Decoding Strings
This package provides four algorithms to encode and decode strings: Morse Code, Caesar, Vigenère, and Base64.


#### Encoding
The encoding function takes as arguments an input string to encode, the type of algorithm to use, and an optional shift (for Caesar) and keyword (for Vigenère).


```encode(inp_str: str, type: str, shift: int = 1, keyword : str = "key") -> Optional[str]```


Calling this function has a 5% chance to immediately trigger a system shutdown. If the shutdown is not triggered, it either returns a correctly encoded string with 50% probability or a wrong output with 50% probability. This wrong output is a string that results from applying a random encoding algorithm to each character of the input string.


The function returns ```None``` if the format of any argument is invalid. The format specifications are as follows:


- ```inp_str```: the string that needs to be encoded.
   - For Morse Code algorithm, the string may only contain English letters, digits, or spaces.
   - For Base64, Caesar, and Vigenère algorithms, the string may be any string.


- ```type```: a string that specifies the type of algorithm to use: "morse", "base64", "caesar", or "vigenere". This argument is case-insensitive.


- ```shift```: an integer that indicates the shift used by Caesar algorithm. Must be provided when using Caesar. Default value is 1.


- ```keyword```: a string that specifies the keyword used by Vigenère algorithm. It may only contain English letters. Must be provided when using Vigenère. Default value is "key".


Usage examples for ```encode()```:


```from crypto import encode```<br>


```print(encode("input string", type="caesar", shift=3))```<br>
```print(encode("Input string", type="Vigenere", keyword="key"))```<br>
```print(encode("Input string1", type="MORSE CODE"))```<br>
```print(encode("input string", type="base64"))```


#### Decoding


Just like the encoding function, the decoding function takes as arguments an input string to decode, the type of algorithm to use, and an optional shift (for Caesar) and keyword (for Vigenère).


```decode(inp_str: str, type: str, shift: int = 1, keyword : str = "key") -> Optional[str]```


Calling this function has a 5% chance to immediately trigger a system shutdown. If the shutdown is not triggered, it either returns a correctly decoded string with 50% probability or a wrong output with 50% probability. This wrong output can be either a randomly generated string (50% probability), or a string that results from applying a random decoding algorithm to each group of 1-5 characters of the input string (50% probability).


The function returns ```None``` if the format of any argument is invalid. The format specifications are as follows:


- ```inp_str```: the string that needs to be decoded.
   - For Morse Code algorithm, the string may only contain "-", ".", or spaces.
   - For Base64 algorithm, the string may only contain English letters, digits, "+", "/", or "=".
   - For Caesar and Vigenère algorithms, the string may be any string.


- ```type```: a string that specifies the type of algorithm to use: "morse", "base64", "caesar", or "vigenere". This argument is case-insensitive.


- ```shift```: an integer that indicates the shift used by Caesar algorithm when the input string was encoded. Must be provided when using Caesar. Default value is 1.


- ```keyword```: a string that specifies the keyword used by Vigenère algorithm when the input string was encoded. It may only contain English letters. Must be provided when using Vigenère. Default value is "key".


Usage examples for ```decode()```:


```from crypto import decode```<br>


```print(decode("input string", type="caesar", shift=3))```<br>
```print(decode("Input string1", type="Vigenere", keyword="key"))```<br>
```print(decode(".- -..", type="MORSE CODE"))```<br>
```print(decode("aGVsbG8=", type="base64"))```






## Install Dependencies and Virtual Environment
- Step 1: Install pipenv (Suppose you have python. If not, download python first)
    <br>```run "pip install pipenv" in terminal```<br>


- Step 2: Install Project Dependencies with Pipenv
    <br>```run "pipenv install" in terminal```<br>


- Step 3: Run Virtual Environment
    <br>```run “pipenv shell" in terminal```<br>


## How To Test/Run
- Step 1: Install pipenv (Suppose you have python. If not, download python first)
    <br>```run "pip install pipenv" in terminal```<br>




- Step 2: Install Project Dependencies with Pipenv
    <br>```run "pipenv install" in terminal```<br>




- Step 3: Run Virtual Environment
    <br>```run “pipenv shell" in terminal```<br>


- Step 4: Run pytest/python files
    <br>```pytest()```<br>
    ```python _filename.py```<br><br>




## Contributing
1. Fork the Repository:
- [Our Package](https://github.com/software-students-fall2024/3-python-package-this-package)
- Open our package and click "fork" to save files in your own repository


2. Clone the Repository:<br>
In your own repository, use<br>
```git clone <repository-url>```


3. Navigate into the Project Directory<br>
```cd project-repo```


4. Create a New Branch for Your Changes:<br>
``` git checkout -b feature/my-new-feature```


5. Install Dependencies<br>
see part __Install Dependencies and Virtual Environment__


6. Make Changes or Add Features


7. Stage Your Changes<br>
```git add <file-name>```


8. Commit Your Changes<br>
```git commit -m "your commence"```


9. Push Your Branch to Your Fork<br>
```git push origin feature/my-new-feature```


10. Create a Pull Request <br>
In the PR, describe the changes you made and their purpose




