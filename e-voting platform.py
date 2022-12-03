def election():
    print('welcome to may 2023 presidential elections')
    print('Here are your candidates:')
    print(' ')
    
    
def display_candidates():
    options =['Tinubu','Atiku','Obi']
    for theifs in range(len(options)):
        print(options[theifs])

def instructions():
    print(' ')
    print('To vote for Tinubu ENTER 0 ')
    print('To vote for Atiku ENTER 1')
    print('To vote for Obi ENTER 2 ')
    

def election_day():
    Tinubu_votes = 0
    Atiku_votes = 0
    Obi_votes = 0
    
    options =['Tinubu','Atiku','Obi']
    
    voter_id = [0,1,2,3,4,5,6,7,8,9]
    
    no_of_voters = len(voter_id)
    
    while True: 
        if voter_id == []:
                Tinubu_percent = (Tinubu_votes / no_of_voters)* 100
                Atiku_percent = (Atiku_votes / no_of_voters)* 100 
                Obi_percent = (Obi_votes / no_of_voters)* 100
                top_dog_percent =(Atiku_percent,Tinubu_percent,Obi_percent)
                top_dog_percent_max = max(top_dog_percent)
                if  top_dog_percent_max == Atiku_percent:
                    top_dog = 'Atiku'
                if  top_dog_percent_max == Tinubu_percent:
                    top_dog = 'Tinubu'
                if  top_dog_percent_max == Obi_percent:
                    top_dog = 'Obi'
                print(top_dog,' is the  new President of Nigeria ','with',top_dog_percent_max,'%  of the total votes')
                break
        else:
            try:
                print(voter_id)
                voter = int(input('please enter your voter ID:'))
                if not 0 <= voter <= 9:
                    raise ValueError()
            except ValueError: 
                print('invalid voter id')
                continue
            else:
                print('you are eligible to vote')
                
            choice = int(input('Please Cast Your Vote:' ))    
            if choice == 1:
                voter_id = voter_id.pop(voter)
                Tinubu_votes +=1
                print('Thank You For Voting')
                print(Tinubu_votes)
            elif choice == 2:
                voter_id = voter_id.pop(voter)
                Atiku_votes += 1
                print('Thank you for Voting')
                print(' ')
                print(Atiku_votes)
            elif choice == 3:
                voter_id = voter_id.pop(voter)
                Obi_votes += 1 
                print('Thank you for Voting') 
                print(' ')
                print(Obi_votes)      
            else:
                print('Please select a valid candidate')
            
            
election_day()

