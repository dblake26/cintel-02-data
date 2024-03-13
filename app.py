import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins # This package provides the Palmer Penguins dataset

# ------------------------------------------------------
Get the Data
# ------------------------------------------------------
# Column names for the penguins data set include: 
# - species: penguin species
# - island: island name 
# - bill_length_mm: length of the bill in millimeters
# - bill_depth_mm: depth of the bill in millimeters
# - flipper_length_mm: length of the flipper in millimeters
# - body_mass_g: body mass in grams
# - sex: MALE or FEMALE

# Load the dataset into the pandas dataframe
# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# ------------------------------------------------------
# Define User Interface (ui)
# ------------------------------------------------------
ui.page_opts(title="Penguin Data DBlake", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
