from flask import Flask, render_template

app = Flask("DBWebApp")


@app.route("/search_products")
def search_products():
    form = [
        {
            "name": "name",
            "title": "Name",
            "type": "text",
        },
        {
            "name": "price",
            "title": "Price",
            "type": "text",
        },
        {
            "name": "firm",
            "title": "Firm",
            "type": "select",
        },
    ]

    return render_template(
        "search.html",
        active="search-products",
        form=form,
    )


@app.route("/search_storages")
def search_storages():
    form = [
        {
            "name": "name",
            "title": "Name",
            "type": "select",
        },
        {
            "name": "address",
            "title": "Address",
            "type": "select",
        },
    ]

    return render_template(
        "search.html",
        active="search-storages",
        form=form,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)

