import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.function
def fizzbuzz(n: int) -> str:

    if not isinstance(n, int) or n <= 0:
        raise ValueError("fizzbuzz expects a strictly positive integer")

    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)


if __name__ == "__main__":
    app.run()
