# Imports
from pathlib import Path
from shiny import reactive, render, req
from shiny.express import input, ui
from shinywidgets import render_plotly
import pandas as pd
import plotly.express as px


# Import data
kbo_file = Path(__file__).parent/'kbopitchingdata.csv'
kbo_df = pd.read_csv(kbo_file)

# UI page options
ui.page_opts(title='Stevens: Korean Baseball Organization (KBO) Pitching Stats', fillable=True)

# === UI Sidebar ==============================================================================
with ui.sidebar(open='open'):
    
    # Include a header
    ui.h2('Korean Baseball Organization Pitching Stats')

    # Choose at least one input user can interact with to filter data
    #-> Select a year
    with ui.card(full_screen=True):
        ui.input_select('selected_year', 'Select a Year',
                       [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 
                        1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 
                        2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
                        2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
    
    #-> Select one or more teams
    with ui.card(full_screen=True):
        ui.input_checkbox_group('selected_teams', 'Select a Team',
                               [
                               'Binggre Eagles', 'Chungbo Pintos',
                               'Doosan Bears', 'Haitai Tigers',
                               'Hanwha Eagles', 'Hyundai Unicorns',
                               'Kia Tigers', 'Kiwoom Heroes',
                               'KT Wiz', 'LG Twins',
                               'Lotte Giants', 'MBC Blue Dragons',
                               'NC Dinos', 'Nexen Heroes',
                               'OB Bears', 'Pacific Dolphins',
                               'Sammi Superstars', 'Samsung Lions',
                               'SK Wyverns', 'Ssangbangwool Raiders',
                               'SSG Landers', 'Woori Heroes'
                               ],
                               selected = 'Binggre Eagles',
                               inline = True)

# === UI Main =================================================================================

# Table/Grid
with ui.card(full_screen=True):
    @render.data_frame
    def table_filtered_data():
        return render.DataGrid(filtered_data())

# Chart
with ui.card(full_screen=True):
    @render_plotly
    def scatter_filtered_data():
        return px.scatter(data_frame = filtered_data(),
                  x = 'ERA',
                  y = 'wins',
                  color = 'team',
                  title = 'ERA vs Wins',
                  labels = {'ERA': 'ERA',
                           'wins': 'Number of wins'}
                 )


# --- Reactive Calc Functions ------------------------------------------------------------------
@reactive.calc
def filtered_data():
    # Make sure at least one team is selected
    #-> We don't have to check if one year is selected because one already is
    req(input.selected_teams())

    # Grab the selected year
    checked_year = kbo_df['year'] == int(input.selected_year())

    # Grab the selected teams
    checked_teams = kbo_df['team'].isin(input.selected_teams())
    
    # Return the teams
    return kbo_df[checked_year & checked_teams]
