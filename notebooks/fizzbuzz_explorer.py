import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from fizzbuzz_tdd_kata import fizzbuzz

    return (fizzbuzz,)


@app.cell
def _(mo):
    n = mo.ui.number(start=1, stop=100, value=15, label="pick a num")
    n
    return (n,)


@app.cell
def _(fizzbuzz, mo, n):
    result = fizzbuzz(n.value)
    mo.md(f"fizzbuzz result: {result}")
    return


@app.cell
def _(fizzbuzz):
    import matplotlib.pyplot as plt

    values = range(1, 31)
    results = [fizzbuzz(i) for i in values]

    plt.figure(figsize=(10, 4))
    plt.bar(values, [len(r) for r in results])
    plt.xlabel("number")
    plt.ylabel("length of fizzbuzz result")
    plt.title("fizzbuzz result lengths")
    plt.show()
    return (plt,)


@app.cell
def _(fizzbuzz, mo):
    # showing numbers n their results
    # data=[(i,fizzbuzz(i)) for i in range(1,16)]
    # data

    mo.ui.table([{"Number": i, "Results": fizzbuzz(i)} for i in range(1, 16)])
    return


@app.cell
def _(fizzbuzz):
    counts = {
        "Fizz": sum(fizzbuzz(i) == "Fizz" for i in range(1, 31)),
        "Buzz": sum(fizzbuzz(i) == "Buzz" for i in range(1, 31)),
        "FizzBuzz": sum(fizzbuzz(i) == "FizzBuzz" for i in range(1, 31)),
    }
    counts
    return (counts,)


@app.cell
def _(counts, plt):
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Result")
    plt.ylabel("count")
    plt.title("fizzbuzz results from 1 to 30")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
