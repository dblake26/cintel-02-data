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


# -------------------------------------------------------
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins # This package provides the Palmer Penguins dataset
import pandas as pd 
import seaborn as sns
from shiny import reactive, render, req

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

#name the page
ui.page_opts(title="Penguin Data Desiree Blake", fillable=True)
        
# Add a Shiny UI sidebar for user interaction
# Use the ui.sidebar() function to create a sidebar
# Set the open parameter to "open" to make the sidebar open by default
# Use a with block to add content to the sidebar

with ui.sidebar(open="open"):  # Set the open parameter to "open" to make the sidebar open by default
    # Add a second-level header to the sidebar
    ui.h2("Sidebar")

# Use ui.input_selectize() to create a dropdown input to choose a column
#   pass in three arguments:
#   the name of the input (in quotes), e.g., "selected_attribute"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) 
    ui.input_selectize(
        "selected_attribute", 
        "Select Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    )

# Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
#   pass in two arguments:
#   the name of the input (in quotes), e.g. "plotly_bin_count"
#   the label for the input (in quotes)
    ui.input_numeric("plotly_bin_count", "Number of Plotly Histogram Bins", 30)

# Use ui.input_slider() to create a slider input for the number of Seaborn bins
#   pass in four arguments:
#   the name of the input (in quotes), e.g. "seaborn_bin_count"
#   the label for the input (in quotes)
#   the minimum value for the input (as an integer)
#   the maximum value for the input (as an integer)
#   the default value for the input (as an integer)
    ui.input_slider("seaborn_bin_count", "Number of Seaborn Bins", 1, 100, 20)

# Use ui.hr() to add a horizontal rule to the sidebar
    ui.hr()

# Use ui.input_checkbox_group() to create a checkbox group input to filter the species
#   pass in five arguments:
#   the name of the input (in quotes), e.g.  "selected_species_list"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) as ["Adelie", "Gentoo", "Chinstrap"]
#   a keyword argument selected= a list of selected options for the input (in square brackets)
#   a keyword argument inline= a Boolean value (True or False) as you like
    ui.input_checkbox_group(
        "selected_species_list", 
        "Select Species", 
        ["Adelie", "Gentoo", "Chinstrap"], selected=["Adelie"], inline=False
    )



# Use ui.a() to add a hyperlink to Github
    ui.a("GitHub", href="https://github.com/dblake26/cintel-02-data", target="_blank")

# When passing in multiple arguments to a function, separate them with commas.

# Creates a DataTable showing all data

with ui.layout_columns(col_widths=(4, 8)):        
    with ui.card():
        "DataTable"

    ui.h2("Penguins Table")

    @render.data_frame
    def render_penguins_table():
        return penguins_df

@render.data_frame
def penguins_data():
    return render.DataGrid(penguins_df, row_selection_mode="multiple") 

# Creates a Plotly Histogram showing all species

with ui.card(full_screen=True):
    ui.card_header("Plotly Histogram")
    
    @render_plotly
    def plotly_histogram():
        return px.histogram(
            penguins_df, x=input.selected_attribute(), nbins=input.plotly_bin_count()
        )

# Creates a Seaborn Histogram showing all species

with ui.card(full_screen=True):
    ui.card_header("Seaborn Histogram")

    @render.plot(alt="Seaborn Histogram")
    def seaborn_histogram():
        histplot = sns.histplot(data=penguins_df, x="body_mass_g", bins=input.seaborn_bin_count())
        histplot.set_title("Palmer Penguins")
        histplot.set_xlabel("Mass")
        histplot.set_ylabel("Count")
        return histplot

# Creates a Plotly Scatterplot showing all species

with ui.card(full_screen=True):
    ui.card_header("Plotly Scatterplot: Species")

    @render_plotly
    def plotly_scatterplot():
        return px.scatter(penguins_df,
            x="bill_length_mm",
            y="body_mass_g",
            color="species",
            title="Penguins Plot",
            labels={
                "bill_length_mm": "Bill Length (mm)",
                "body_mass_g": "Body Mass (g)",
            },
            size_max=8, 
                         )
