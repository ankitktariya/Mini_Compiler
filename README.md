#  Smart Compiler - Mini Domain Specific Language Compiler

Smart Compiler is a lightweight, modular, and beginner-friendly DSL compiler built using Python (Flask) for backend and React for frontend. It supports:

-  Math Expression Evaluation
-  Markdown to HTML Conversion
-  SQL-like Query Execution on CSV Files

---

##  Features

 Evaluate arithmetic and advanced math expressions  
 Convert user-written markdown into clean HTML (supports headings, bold, italic, links, images)  
 Execute simple SELECT queries with WHERE conditions on CSV files  
 Easy-to-use web interface with live result preview  
Fully modular architecture (Lexer, Parser, Evaluator separated)

---

##  Folder Structure
Smart_Compiler/
├── backend/
│ ├── app.py
│ ├── core/
│ │ ├── math_evaluator.py
│ │ ├── markdown_parser.py
│ │ ├── sql_lexer.py
│ │ ├── sql_parser.py
│ │ └── sql_executor.py
│ └── sample.csv
│
├── frontend/
│ ├── App.jsx
│ ├── index.css
│ └── main.jsx
│
├── README.md
└── requirements.txt
