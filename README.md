# 🧠 Brainfuck Interpreter (Python)

A simple but efficient [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter written in Python.  
Supports 8-bit cells, dynamic tape growth, and precomputed loop jumps for better performance on loop-heavy programs like Mandelbrot.

---

## ✨ Features
- **Pure Python 3** implementation  
- **Precomputed bracket jumps** for fast loops  
- **Dynamic tape** (grows on demand)  
- **Standard Brainfuck commands**: `> < + - . , [ ]`  
- **Runs real Brainfuck programs** like `hello.bf`

---

## 📂 Project structure

```

bf-interpreter/
│── bf/
│       ├── __init__.py
│       ├── __main__.py      # CLI entry point
│       └── interpreter.py   # Interpreter class
├── pyproject.toml
├── README.md
└── hello.bf                  # Example Brainfuck program

````

---

## 🚀 Usage

### Run with Python
From the project root:

```bash
python -m bf hello.bf
````

Where `hello.bf` is any Brainfuck source file.

### Example: Hello World

Create a file `hello.bf` with:

```
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++.>.+++.------.--------.>+.>.
```

Then run:

```bash
python -m bf hello.bf
```

Output:

```
Hello World!
```



## 🛠 Development

* Requires **Python 3.9+**
* Run tests/examples with:

  ```bash
  python -m bf hello.bf
  ```

---

## 📜 License

This project is open-source.
---

