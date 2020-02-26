## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## greet with name
* given_name
  - utter_greet_with_name

## greet with name
* vi_to_en
  - give_vi_to_en

## greet with name
* en_to_vi
  - give_en_to_vi

## greet with name
* en_to_en
  - give_en_to_en

## reply name
# ask_name
  - utter_rep_name
