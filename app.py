import streamlit as st
import requests

st.set_page_config(page_title="Live Cricket Score", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1540747913346-19e32dc3e97e");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    h1, h2, h3, p, div {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏏 LIVE CRICKET SCORE")
page = st.sidebar.selectbox(
    "Select Section",
    [
    "Home",
    "Live Scores",
    "Recent Matches",
    "IPL Matches"
    ]
)
if page == "Home":

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align:center;'>🏏 LIVE CRICKET HUB</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>Live Scores • Recent Matches • IPL Matches</h3>",
        unsafe_allow_html=True
    )

    #st.stop()
url = "https://crickbuzz-official-apis.p.rapidapi.com/matches/live"

headers = {
    "x-rapidapi-key": "bb08b27952msh1010980cd0ad554p1ba16ejsn810e47bf639b",
    "x-rapidapi-host": "crickbuzz-official-apis.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
#st.write(response.status_code)
#st.json(response.json())

data = response.json()

#st.json(data)

if page ==  "Live Scores":
  st.write("LIVE SCORES PAGE")

  if "typeMatches" in data:

    for series in data["typeMatches"]:

        for match in series["seriesMatches"]:

            if "seriesAdWrapper" in match:

              for m in match["seriesAdWrapper"]["matches"]:

                team1 = m["matchInfo"]["team1"]["teamName"]
                team2 = m["matchInfo"]["team2"]["teamName"]

                st.subheader(f"{team1} vs {team2}")

                if "matchScore" in m:

                   if "team1Score" in m["matchScore"]:

                    t1 = m["matchScore"]["team1Score"]["inngs1"]
                    runs1 = t1.get("runs", 0)
                    wickets1 = t1.get("wickets", 0)
                    overs1 = t1.get("overs", 0)

                    st.write(
                      f"{team1}: {runs1}/{wickets1} ({overs1} overs)"
                  )

                   if "team2Score" in m["matchScore"]:

                     t2 = m["matchScore"]["team2Score"]["inngs1"]
                     runs2 = t2.get("runs", 0)
                     wickets2 = t2.get("wickets", 0)
                     overs2 = t2.get("overs", 0)

                     st.write(
                        f"{team2}: {runs2}/{wickets2} ({overs2} overs)"
                       )

              st.write("---")
st.markdown("---")
st.header("India Recent Matches")

recent_url = "https://crickbuzz-official-apis.p.rapidapi.com/matches/recent"
recent_response = requests.get(recent_url, headers=headers)
recent_data = recent_response.json()

st.markdown("---")
st.header("India & IPL Recent Matches")

if "typeMatches" in recent_data:

    for series in recent_data["typeMatches"]:

        for match in series["seriesMatches"]:

            if "seriesAdWrapper" in match:

                for m in match["seriesAdWrapper"]["matches"]:

                    team1 = m["matchInfo"]["team1"]["teamName"]
                    team2 = m["matchInfo"]["team2"]["teamName"]

                    series_name = match["seriesAdWrapper"].get("seriesName", "")

                    if (
                        "India" in team1
                        or "India" in team2
                        or "IPL" in series_name
                        or "Indian Premier League" in series_name
                    ):

                        st.subheader(f"{team1} vs {team2}")
                        st.write(f"Series: {series_name}")

                        if "matchScore" in m:

                         if "team1Score" in m["matchScore"]:
                            t1 = m["matchScore"]["team1Score"]["inngs1"]

                            st.write(
                               f"{team1}: {t1.get('runs',0)}/{t1.get('wickets',0)} ({t1.get('overs',0)} overs)"
                               )

                        if "team2Score" in m["matchScore"]:
                          t2 = m["matchScore"]["team2Score"]["inngs1"]

                          st.write(
                             f"{team2}: {t2.get('runs',0)}/{t2.get('wickets',0)} ({t2.get('overs',0)} overs)"
                              )

                          st.write("----")
