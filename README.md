# Gemini Text to SQL

A local Flask application that turns English or Arabic questions into Microsoft SQL Server SELECT queries using Gemini. Review generated SQL before choosing to execute it and display a table of results.

## Workflow

Natural-language question → schema-aware prompt → Gemini → SQL validation → query preview → optional execution → result table.

## Example questions

The included schema example describes a Student table. Example requests include:

- List the five departments with the most students.
- Show the average student age for each department with at least five students.
- List up to ten students older than 22, ordered by age descending.
- اعرض عدد الطلبة ومتوسط السن في كل قسم، ورتّب الأقسام حسب عدد الطلبة.

These are prompts to try, not claims of successful model execution.

## Setup

1. Install Python 3.10+ and `pip install -r requirements.txt`.
2. Copy `.env.example` to `.env`, add your own Gemini key, and choose a model available to your account.
3. Create `schema.sql` containing the **actual** tables and columns in your database. `schema.example.sql` shows the Student schema from the supplied notebook. The supplied brief instead requests Company_SD; its actual schema and database backup are not included. Update both your schema file and database connection to match.
4. Run `python app.py` and open `http://127.0.0.1:5001`.
5. Generate and review SQL. Execution stays disabled by default.
6. To enable execution, install ODBC Driver 17 or 18 for SQL Server, configure `SQL_CONNECTION_STRING` for a dedicated SELECT-only database user, and set `ENABLE_QUERY_EXECUTION=true`. For example, use `Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=Company_SD;UID=YOUR_READ_ONLY_USER;PWD=YOUR_PASSWORD;` in your local environment, never in committed code.

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Local Flask interface |
| `text_to_sql.py` | Prompt, generation, validation, execution |
| `templates/index.html` | Question, SQL preview, results |
| `text_to_sql_demo.ipynb` | Interactive generation examples |
| `schema.example.sql` | Student schema illustration |
| `.env.example` | Configuration placeholders |
| `docs/project_brief.pdf` | Supplied project specification |

## Execution limits

The validator accepts a single parsed SELECT, rejects writes and SELECT INTO, and restricts cross-database references and unrecognized functions. It is a guardrail, not a SQL sandbox or an authorization system. A SELECT-only database login is required for execution. Schema text is sent to Gemini with the question; database results are displayed locally and are not sent back by this code.

The app is intended for local use, without authentication or production deployment. Result display is capped at 100 rows and queries have a timeout, but this does not guarantee low-cost execution. Do not expose it publicly as-is.

## Preparation changes and validation

The uploaded notebook contained mixed API experiments and a Flask route referencing missing HTML templates. This repository focuses on its Text-to-SQL workflow, adds the template, moves credentials to environment variables, provides clearer prompts and examples, and separates generation from execution. Notebook outputs are cleared. No API key, database rows, or database backup is included.

Python syntax was checked. Live Gemini calls and SQL Server execution have not been verified here. Setup requires your API account, actual database schema, and database credentials.

SDK reference: https://ai.google.dev/gemini-api/docs/quickstart
