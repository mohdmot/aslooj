<p align="center">
  <img src="https://github.com/mohdmot/aslooj/blob/main/logo.png?raw=true">
</p>
<h1 align="center">Aslooj Programming Language</h1>

Aslooj is an emojis programming language. It contains some commands that can be written and given parameters. I wrote this project a long time ago, but today I added a function command to it and thought about uploading it to GitHub. This project is just for fun.

## Installation
The program only works fully on Windows. The color change command only works on Windows
- Download EXE from [/executable](https://github.com/mohdmot/aslooj/tree/main/executable)
- Run CMD
- Run Your File
```
aslooj myFile.as
```

## Coding
- **Print To Console**

  For Printing any thing, use lollipop emoji `🍭` :
```py
🍭 <Hello World !!>
🍭 <I am>, 16, <years old>
```
  String writted inside `<>`, numbers writted normally.

- **Define a Variable**

  Defining variables is done using the alien emoji `👽`, then the variable name, then its value. This syntax is always constant
```py
👽 i 0
👽 name <mohammed>
```

- **Take an Input**

  We can take input from the user through the console, and store it in a variable, using the crying emoji `😭`. You write the emoji, then the name of the variable you want to store in, then the text that will appear to the user.
```py
😭 name <What is Your Name ?>
😭 age <How old are you?>
🍭 <Hi>, name, <, You are>, age, <year old>    # print inputs
```

- **Performing Calculations on Variables**

  You can define a variable with the alien emoji as we explained previously, and then perform a mathematical operation on it, With smiling cat emoji `😼`, such as: `+` , `-` `/` , `*` .
```py
👽 i 2
😼 i + 1
😼 i * 5
```
There must be a space between the emoji, the variable name, the mathematical sign, and the number

- **Sleeping**

You can use the sleeping emoji `😴` to pause the program for a few seconds.
```py
😴 5
```

- **Exit**

  Use the monster emoji `👹` to stop the program permanently.
```py
👹
```

- **Changing Color**

  This command works on Windows systems only. It is used to change the color of text in the console, using the happy cat emoji `😺`. The available colors are: `⚫️ 🔴 🟡 🟢 🔵 🟣 ⚪️`.
```py
😺 🟡
```

- **Define and Call Functions**

  We can collect some lines of code inside a function, and then call them with the robot’s emoji `🤖`. To define the function, you write the emoji, then the name of the function, then `:`, and the lines belonging to the function are after an indent space (Tab).
```py
🤖 askUser :
	😭 NAME <What is Your Name ? >   # take input
	🍭 <Hello>,NAME,<Chan !!>        # print text
```
**Note:** Any text written after `#` is considered a comment and does not affect the code.

Now the function is defined with the name `askUser`. To call it, we use the same emoji and then the name of the function only, without `:`.
```py
🤖 askUser
```
The function will simply run
