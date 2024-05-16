import java.util.Scanner;
import java.util.ArrayList;

public class blackjack {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        ArrayList<String> cards = new ArrayList<String>();
        ArrayList<String> removedCards = new ArrayList<String>();
        boolean run = true;
        int money = 200;
        int bet = 0;
        String[] suits = {"Hearts", "Diamonds", "Spades", "Clubs"};
        String[] nums = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
        
        for (String suit : suits){
            for (String num : nums){
                cards.add(num + " of " + suit);
            }
        }

        while (run){
            //betting
            System.out.print("Enter your bet: ");
            bet = input.nextInt();
            while(bet > money){
                System.out.println("Cannot bet that!");
                System.out.print("Enter new bet: ");
                bet = input.nextInt();
            }

            //dealing cards
            int rand = (int) (Math.random() * (cards.size() - 1));
            String hold = cards.remove(rand);
            ArrayList<String> myCards = new ArrayList<String>();
            myCards.add(hold);
            removedCards.add(hold);
            System.out.println("Your card is " + myCards.get(0));

            rand = (int) (Math.random() * (cards.size() - 1));
            hold = cards.remove(rand);
            ArrayList<String> dealersCards = new ArrayList<String>();
            dealersCards.add(hold);
            removedCards.add(hold);
            System.out.println("Dealer's card is " + dealersCards.get(0));

            rand = (int) (Math.random() * (cards.size() - 1));
            hold = cards.remove(rand);
            myCards.add(hold);
            removedCards.add(hold);
            System.out.println("Your next card is " + hold);
            System.out.println("Your cards are " + myCards.get(0) + " and " + myCards.get(1));

            //player blackjack check
            boolean playerBlackjack = false;
            if(myCards.get(0).substring(0, 1).equals("A") || myCards.get(1).substring(0, 1).equals("A")){
                String myFirstCard = myCards.get(0).substring(0,1);
                String mySecondCard = myCards.get(1).substring(0,1);
                if(myCards.get(0).substring(0, 2).equals("10") || myFirstCard.equals("J") || myFirstCard.equals("Q") || myFirstCard.equals("K")){
                    System.out.println("You got blackjack!");
                    playerBlackjack = true;
                }
                if(myCards.get(1).substring(0, 2).equals("10") || mySecondCard.equals("J") || mySecondCard.equals("Q") || mySecondCard.equals("K")){
                    System.out.println("You got blackjack!");
                    playerBlackjack = true;
                }
            }            
            
            rand = (int) (Math.random() * (cards.size() - 1));
            String dealerCard = cards.remove(rand);
            removedCards.add(dealerCard);
            dealersCards.add(dealerCard);

            //dealer blackjack check
            boolean dealerBlackjack = false;
            if(dealersCards.get(0).substring(0, 1).equals("A") || dealersCards.get(1).substring(0, 1).equals("A")){
                String firstCard = dealersCards.get(0).substring(0,1);
                String secondCard = dealersCards.get(1).substring(0,1);
                if(dealersCards.get(0).substring(0, 2).equals("10") || firstCard.equals("J") || firstCard.equals("Q") || firstCard.equals("K")){
                    System.out.println("Dealer got blackjack!");
                    dealerBlackjack = true;
                }
                if(dealersCards.get(1).substring(0, 2).equals("10") || secondCard.equals("J") || secondCard.equals("Q") || secondCard.equals("K")){
                    System.out.println("Dealer got blackjack!");
                    dealerBlackjack = true;
                }
            }

            //blackjack payouts
            if(dealerBlackjack && playerBlackjack){
                System.out.println("You both got it so nothing for you!");
            } else if (playerBlackjack){
                System.out.println("Congratulations!");
                money += (bet * 1.5);
                System.out.println("You have " + money + " money.");
            } else if (dealerBlackjack){
                System.out.println("The dealer had a " + dealersCards.get(0) + " and a " + dealersCards.get(1));
                System.out.println("womp womp :(");
                money -= bet;
                System.out.println("You have " + money + " money.");
            } else{
                while(true){
                    System.out.print("Enter 'h' for hit, 's' for stand, or 'stop' to stop playing: ");
                    String move = input.nextLine();
                    if(move.equals("stop")){
                        System.out.println("Thanks for playing! You ended with " + money + " money!");
                        run = false;
                        break;
                    }
                    if(move.equals("s")){
                        System.out.println("Your score is " + getScore(myCards));
                        int dealer = playDealer(dealersCards, cards, removedCards);
                        if(getScore(myCards) > dealer){
                            System.out.println("You won!");
                            money += bet;
                            System.out.println("You have " + money + " money.");
                            System.out.println();
                            break;
                        } else if(getScore(myCards) == dealer){
                            System.out.println("push");
                            System.out.println("You have " + money + " money.");
                            System.out.println();
                            break;
                        } else if(getScore(myCards) < dealer){
                            System.out.println("you lost womp womp");
                            money -= bet;
                            System.out.println("You have " + money + " money.");
                            System.out.println();
                            break;
                        } else{
                            System.out.println("uh oh!");
                        }
                    } else if(move.equals("h")){
                        hit(cards, myCards, removedCards);
                        System.out.println("Your new score is " + getScore(myCards));
                        if(getScore(myCards) > 21){
                            System.out.println("Bust!");
                            System.out.println("you lost womp womp");
                            money -= bet;
                            System.out.println("You have " + money + " money.");
                            System.out.println();
                            break;
                        }
                    }
                }
            }

            for(String stuff : removedCards){
                cards.add(stuff);
            }
            while(removedCards.size() != 0){
                removedCards.remove(0);
            }

            while(myCards.size() != 0){
                myCards.remove(0);
            }

            while(dealersCards.size() != 0){
                dealersCards.remove(0);
            }

            if(money == 0){
                System.out.println("You're broke!");
                break;
            }
        }
    }

    public static int getScore(ArrayList<String> hand){
        int score = 0;
        int aceCount = 0;
        for(String kard : hand){
            String sub = kard.substring(0, 1);
            if(sub.equals("J") || sub.equals("Q") || sub.equals("K")){
                score += 10;
            } else if(sub.equals("A")){
                score += 11;
                aceCount++;
            } else if(kard.substring(0,2).equals("10")){
                score += 10;
            } else {
                int numero = Integer.parseInt(sub);
                score += numero;
            }
        }
        while(score > 21 && aceCount > 0){
            score -= 10;
            aceCount--;
        }
        aceCount = 0;
        return score;
    }

    public static int playDealer(ArrayList<String> dealer, ArrayList<String> allCards, ArrayList<String> goneCards){
        System.out.println("The dealer has " + dealer.get(0) + " and " + dealer.get(1));
        int dealScore = 0;
        while(true){
            dealScore = getScore(dealer);
            if(dealScore > 16 && dealScore < 22){
                return dealScore;
            } else if (dealScore > 21){
                System.out.println("Bust!");
                return 0;
            } else {
                hit(allCards, dealer, goneCards);
                System.out.println("The dealer's new score is " + getScore(dealer));
            }
        }
    }

    public static boolean dealerHasAce(ArrayList<String> dealerHand){
        for (String thingy : dealerHand){
            String substr = thingy.substring(0, 1);
            if(substr.equals("A")){
                return true;
            }
        }
        return false;
    }

    public static void hit(ArrayList<String> availableCard, ArrayList<String> hands, ArrayList<String> removd){
        int index = (int) (Math.random() * availableCard.size() - 1);
        String addThisCard = availableCard.remove(index);
        hands.add(addThisCard);
        removd.add(addThisCard);
        System.out.println("The added card is a " + addThisCard);
    }
}