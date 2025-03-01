import panel as pn
import seaborn as sns
import hvplot.pandas

# Load the Iris dataset
df = sns.load_dataset('iris')

# Define the widget: dropdown menus for selecting x and y axes
x_selector = pn.widgets.Select(name='X-Axis', options=list(df.columns[:-1]), value='sepal_length')
y_selector = pn.widgets.Select(name='Y-Axis', options=list(df.columns[:-1]), value='sepal_width')

# Define a function that returns a scatter plot based on the selected x and y axes
@pn.depends(x=x_selector, y=y_selector)
def create_scatter_plot(x, y):
    return df.hvplot.scatter(x=x, y=y, by='species', legend='top', height=400, width=400)

# Create a Panel layout
dashboard = pn.Column(
    pn.Row(x_selector, y_selector),
    create_scatter_plot
)

# Serve the dashboard
dashboard.servable()
