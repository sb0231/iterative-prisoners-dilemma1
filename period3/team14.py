####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Rima and Sid'
strategy_name = 'Uhhh Comp Sci Things'
strategy_description = 'Collude for the first two rounds. For all subsequent rounds: locate the most recent round that is equivalent to the previous round and replicate the opponent's move on the round after that. Or else, betray if the opponent had a different choice than us previous round and collude otherwise'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) <= 1:
        return 'c'
    else:
        previous_my = my_history[len(my_history)-1]
        previous_their = their_history[len(their_history-1]

    for i in range(len(their_history)-2, -1, -1): 
       second_to_previous_my = my_history[i]
        second_to_previous_their = their_history[i]
        if (previous_my == second_to_previous_my) and (second_to_previous_their == previous_their):
            return their_history[i+1]
    if previous_my != previous_their:
        return 'b'
    else:
        return 'c'


  
    

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             