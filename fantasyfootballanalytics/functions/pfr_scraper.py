import pandas as pd
import requests
# import definitions as app_def
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


class FProPlayer:
    # Defaults
    def __init__(self, lookup='qb', season='2020', show_max='false', show_min='false', scoring='ppr', week='draft',
                 create_file=False):
        self.lookup = lookup
        self.season = season

        self.__url_proto = 'https'
        self.__url_host = 'www.fantasypros.com/nfl/projections/'
        # url_req_type = 'league'
        self.source_url = '{proto}://{host}/{lookup}.php'.format(proto=self.__url_proto, host=self.__url_host,
                                                                 lookup=self.lookup)
        self.__file = 'fpro{lookup}{year}.csv'.format(lookup=self.lookup, year=self.season)
        self.destination_file = app_def.DATA_PATH.joinpath(self.__file).resolve()

        self.raw_data = None
        self.data_frame = None

        self.params = {
            'max-yes': show_max,
            'min-yes': show_min,
            'scoring': scoring,
            'week': week
        }
        self.header = {
            'qb': ['player', 'passAtt', 'passComp', 'passYds', 'passTds', 'passInt', 'rushAtt',
                   'rushYds', 'rushTds', 'fumbles', 'fpts'],
            'rb': ['player', 'rushAtt', 'rushYds', 'rushTds', 'rec', 'recYds', 'recTds',
                   'fumbles', 'fpts'],
            'wr': ['player', 'rushAtt', 'rushYds', 'rushTds', 'rec', 'recYds', 'recTds',
                   'fumbles', 'fpts'],
            'te': ['player', 'rec', 'recYds', 'recTds', 'fumbles', 'fpts'],
            'k': ['player', 'fg', 'fga', 'xp', 'fpts'],
            'dst': ['player', 'sacks', 'int', 'fumbles recovered', 'fumbles forced', 'TD', 'safety', 'points against',
                    'yards against', 'fpts']
        }
        if create_file:
            self.__scrape()
            self.write_to_csv()
        else:
            try:
                self.data_frame = pd.read_csv(self.destination_file, header=0)
            except Exception as ex:
                print('Exception: ', ex)

    def __scrape(self):  # __ keeps it private
        # returns list of players
        response = requests.get(self.source_url, self.params).content
        # header = list(self.header[self.lookup].values())
        self.raw_data = pd.read_html(str(response), header=None)[0]

    def get_bar_px(self):
        df = self.data_frame.query('fpts > 0')
        fig = px.bar(
            df.sort_values(by=['fpts'], ascending=False),
            x="fpts",
            y="player",
            hover_data=['player'],
            color="player",
            orientation='h',
            template="seaborn"
        )
        return fig

    def get_indicator_px(self, player=''):
        fpts = 0
        if player != '':
            try:
                fpts = float(self.data_frame.query('player==@player')[['fpts']].values)
            except Exception as ex:
                pass

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=fpts,
            title={'text': 'ftps'},
            # template="seaborn",
            domain={'x': [0, 1], 'y': [0, 1]}

        ))
        return fig

    def get_boxplot_px(self, player=''):
        fpts = 0
        if player != '':
            try:
                fpts = float(self.data_frame.query('player==@player')[['fpts']].values)
            except Exception as ex:
                pass

        fig = px.box(
            self.data_frame,
            x='player',
            y="fpts",
            boxmode="overlay",
            points='all',
            template="seaborn",
            orientation='h'
        )
        return fig

    def get_bullet_px(self, player=''):
        fpts, position_median, position_mean, position_max, position_min, q1_df, q2_df = 0, 0, 0, 0, 0, 0, 0

        if player != '':
            try:
                df = self.data_frame.query('fpts > 0')
                # Grab Statistical Summary
                position_median = df[['fpts']].median()[0]
                position_mean = df[['fpts']].mean()[0]
                position_max = df[['fpts']].max()[0]
                position_min = df[['fpts']].min()[0]
                q1_df = df[['fpts']].quantile(.25)[0]
                q2_df = df[['fpts']].quantile(.75)[0]

                fpts = float(df.query('player==@player')[['fpts']].values)
            except Exception as ex:
                pass

        fig = go.Figure(
                go.Indicator
                (
                    mode="number+gauge+delta",
                    value=fpts,
                    delta={'reference': position_mean},
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "fpts"},
                    gauge={
                        'shape': "bullet",
                        'axis': {'range': [None, position_max]},
                        'threshold': {
                            'line': {'color': "red", 'width': 2},
                            'thickness': 0.75,
                            'value': position_mean
                        },
                        'steps': [
                            {'range': [0, q1_df], 'color': "lightgray"},
                            {'range': [q1_df, q2_df], 'color': "gray"},
                            {'range': [q2_df, position_max], 'color': "lightgray"}
                        ]}
                )
        )
        return fig

    def write_to_csv(self):
        try:
            self.raw_data.to_csv(self.destination_file, index=True, header=self.header[self.lookup])
        except Exception as ex:
            print('Exception: ', ex)


class FProQBPlayer(FProPlayer):
    def __init__(self, lookup='qb', season='2020', show_max='false', show_min='false', scoring='ppr', week='draft',
                 create_file=False):
        super().__init__(lookup, season, show_max, show_min, scoring, week, create_file)

    def get_scatter_px(self):
        df = self.data_frame.query('fpts > 0')
        fig = px.scatter(
            df,
            x="passTds",
            y="passYds",
            size='fpts',
            hover_data=['player'],
            color="player",
            template="seaborn"
        )
        return fig

    def get_stats_bar_px(self, player=''):
        col = ['passAtt', 'passComp', 'passYds', 'passTds', 'passInt', 'rushAtt']
        if player != '':
            player_df = self.data_frame.query('player==@player')[['player', 'passAtt', 'passComp', 'passYds',
                                                                  'passTds', 'passInt', 'rushAtt']]
            # player_transposed = player_df.T
            fig = px.bar(
                go.Bar(
                    x=player_df.columns,
                    y=player_df.values,
                    # hover_data=['player'],
                    # color="player",
                ),
                orientation='v',
                template="seaborn"
            )
            return fig
        else:
            return None


class FProRBPlayer(FProPlayer):
    def __init__(self, lookup='qb', season='2020', show_max='false', show_min='false', scoring='ppr', week='draft',
                 create_file=False):
        super().__init__(lookup, season, show_max, show_min, scoring, week, create_file)

    def get_scatter_px(self):
        df = self.data_frame.query('fpts > 0')
        fig = px.scatter(
            df,
            x="rushTds",
            y="rushYds",
            size='fpts',
            hover_data=['player'],
            color="player",
            template="seaborn"
        )
        return fig


class FProWRPlayer(FProPlayer):
    def __init__(self, lookup='qb', season='2020', show_max='false', show_min='false', scoring='ppr', week='draft',
                 create_file=False):
        super().__init__(lookup, season, show_max, show_min, scoring, week, create_file)

    def get_scatter_px(self):
        df = self.data_frame.query('fpts > 0')
        fig = px.scatter(
            df,
            x="recTds",
            y="recYds",
            size='fpts',
            hover_data=['player'],
            color="player",
            template="seaborn"
        )
        return fig


class FProTEPlayer(FProPlayer):
    def __init__(self, lookup='qb', season='2020', show_max='false', show_min='false', scoring='ppr', week='draft',
                 create_file=False):
        super().__init__(lookup, season, show_max, show_min, scoring, week, create_file)

    def get_scatter_px(self):
        df = self.data_frame.query('fpts > 0')
        fig = px.scatter(
            df,
            x="recTds",
            y="recYds",
            size='fpts',
            hover_data=['player'],
            color="player",
            template="seaborn"
        )
        return fig


class FProKPlayer(FProPlayer):
    def __init__(self, lookup='qb', season='2020', show_max='false', show_min='false', scoring='ppr', week='draft',
                 create_file=False):
        super().__init__(lookup, season, show_max, show_min, scoring, week, create_file)

    def get_scatter_px(self):
        fig = px.scatter(
            self.data_frame,
            x="fga",
            y="fg",
            size='fpts',
            hover_data=['player'],
            color="player",
            template="seaborn"
        )
        return fig


class FProDSTPlayer(FProPlayer):
    def __init__(self, lookup='qb', season='2020', show_max='false', show_min='false', scoring='ppr', week='draft',
                 create_file=False):
        super().__init__(lookup, season, show_max, show_min, scoring, week, create_file)

    def get_scatter_px(self):
        fig = px.scatter(
            self.data_frame,
            x="yards against",
            y="points against",
            size='fpts',
            hover_data=['player'],
            color="player",
            template="seaborn"
        )
        return fig


# FPro_QBPlayer2020 = FProPlayer(season='2020', lookup='qb', create_file=True)
# FPro_RBPlayer2020 = FProPlayer(season='2020', lookup='rb', create_file=True)
# FPro_WRPlayer2020 = FProPlayer(season='2020', lookup='wr', create_file=True)
# FPro_TEPlayer2020 = FProPlayer(season='2020', lookup='te', create_file=True)
# FPro_KPlayer2020 = FProPlayer(season='2020', lookup='k', create_file=True)
# FPro_DSTPlayer2020 = FProPlayer(season='2020', lookup='dst', create_file=True)
