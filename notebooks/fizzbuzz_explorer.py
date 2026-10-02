import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
async def _():
    import sys

    if sys.platform == "emscripten":
        import micropip

        await micropip.install("https://uzair017.github.io/fizzbuzz-tdd-kata/public/fizzbuzz_tdd_kata-0.1.0-py3-none-any.whl")
    return


@app.cell
def _():
    from fizzbuzz_tdd_kata import fizzbuzz

    return (fizzbuzz,)


@app.cell
def _():
    from collections import Counter

    return (Counter,)


@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # FizzBuzz Explorer

    Pick a range below and see how fizzbuzz classifies each number in it,
    both as a list and as a chart of the distribution of outputs.

    This notebook uses the `fizzbuzz_tdd_kata` package instead of reimplementing
    the function.
    """)
    return


@app.cell
def _(mo):
    start = mo.ui.slider(1, 200, value=1, label="range start")

    end = mo.ui.slider(1, 200, value=100, label="range end")

    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, fizzbuzz, start):
    lo, hi = sorted((start.value, end.value))
    results = [fizzbuzz(n) for n in range(lo, hi + 1)]
    results
    return (results,)


@app.cell
def _(Counter, plt, results):
    counts = Counter("number" if r.isdigit() else r for r in results)

    fig, ax = plt.subplots()

    ax.bar(counts.keys(), counts.values(), color=["#4c72b0", "#dd8452", "#55a868", "#c44e52"])
    ax.set_ylabel("count")
    ax.set_title("distribution of fizzbuzz outputs over the selected range")

    fig
    return


@app.cell
def _(fizzbuzz, mo):
    # showing numbers n their results
    # data=[(i,fizzbuzz(i)) for i in range(1,16)]
    # data

    mo.ui.table([{"Number": i, "Results": fizzbuzz(i)} for i in range(1, 16)])
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
