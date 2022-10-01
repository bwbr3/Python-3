import unittest
def get_wager(chips):
    chips = (range(1,99))
    return 1

if __name__ == "__main__":
    
    results = input('How many chips do you want to start with?')
    output = get_wager(results)
    print(output)
    for i in range(99):
      if i > 1:
        print('Too Low value, you can only choose 1 - 100 chips')

      elif i > 100:
            
        print('Too High value, you can only choose 1 - 100 chips')


def get_slot_results ():
    return 1, 2, 3
def get_slot_macthes(reel1, reel2, reel3):
    results = get_matches(3,3,3)
    self.assertEqual(results)
    result = getmatches
 
    return 0
    

def get_payout(wager, matches):
    
    results = get_payout(3,0)
    self.assertEqual(-3, results)
    results = get_payout(2, 3)
    self.asserEqual(18, results)
    results = get_payout(5,2)
    self.assertEqual(10,resluts)
    
    return wager * -1


def get_bank():
    return 0 

if __name__ == "__main__":
    __unittest = True
    unittest.main()
    

def play_again() -> bool:

    user_input = ['Yes']
    with patch('sys.stdout', new_callable=StringIO):
        with patch('builtins,input', side_effect = user_input):
            results = lab05.play_again()
        self.assertTrue(results)

    
playing = True
while playing:
    bank = get_bank()
while True:
     wager = get_wager(bank)
     reel1, reel2, reel3 = get_slot_results()
     matches = get_matches(reel1, reel2, reel3)
     payout = get_payout(wager, matches)
     bank = bank + payout
     print("Your spin", reel1, reel2, reel3)
     print("You matched", matches, "reels")
     print("You won/lost", payout)
     print("Current bank", bank)
     print()
           
     print("You lost all", 0, "in", 0, "spins")
     print("The most chips you had was", 0)
     playing = play_again()

            
           



    



