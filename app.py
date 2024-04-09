# Imports
from shiny import reactive, render
from shiny.express import ui
from shinywidgets import render_widget
import pandas as pd

# UI page options
ui.page_opts(title='Korean Baseball Organization (KBO) Pitching Stats', fillable=True)
# === UI Sidebar ==============================================================================
with ui.sidebar():
# (
    # Include a header
    ui.h2('Korean Baseball Organization Pitching Stats')

    # Choose at least one input user can interact with to filter data
    #-> Select one or more teams
    with ui.card(full_screen=True):
        ui.input_checkbox_group('teams', 'Select a Team',
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
                               ])
    #-> Select a year
    with ui.card(full_screen=True):
        ui.input_select('year', 'Select a Year',
                       [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
                       1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
                       2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
                       2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
# )

# === UI Main =================================================================================

# Basic dashboard template
#-> What to show:
#--> year, team, average_age, runs_per_game, wins, losses, ERA, shutouts, innings_pitched, hits
#--> runs, earned_runs, home_runs, walks, strikeouts, hit_batter, WHIP

    # Output text
    #-> Cards

    # Table / Grid

    # Chart
    #-> ipywidgits


# --- Function to Read in File -----------------------------------------------------------------
@reactive.file_reader
def kbo_df():
    return pd.read_csv('C:/Users/Public/Documents/kbopitchingdata.csv')

# --- Reactive Calc Function -------------------------------------------------------------------

# Similar to project 3
