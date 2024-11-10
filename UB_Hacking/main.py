from scraping import scraper
from bias_counter import bias_stats
from data_reader import read_data

def main():
    continue_run = True
    while continue_run:
        url = input("Enter Gale Database URL: ")
        txt = scraper(url)
        score = bias_stats(txt, read_data())
        total_score = score[0]
        total_keywords = score[1]
        avg = score[2]

        if (total_keywords <= 10 or (avg >= -2 and avg <= 2)):
            print("The given article has a neutral bias.")
        elif (avg < -2):
            if (avg < -8):
                print(f"This article has an extreme left-leaning bias, leaning {50 + (abs(round(avg, 2)) *5 )}% Democrat.")
            elif (avg < -5):
                print(f"This article has a moderately left-leaning bias, leaning {50 + (abs(round(avg, 2)) *5 )}% Democrat.")
            else:
                print(f"This article has a slightly left-leaning bias, leaning {50 + (abs(round(avg, 2)) *5 )}% Democrat.")
        elif (avg > 2):
            if (avg > 8):
                print(f"This article has an extreme right-leaning bias, leaning {50 + (abs(round(avg, 2)) *5 )}% Republican.")
            elif (avg > 5):
                print(f"This article has a moderately right-leaning bias, leaning {50 + (abs(round(avg, 2)) *5 )}% Republican.")
            else:
                print(f"This article has a slightly right-leaning bias, leaning {50 + (abs(round(avg, 2)) *5 )}% Republican.")
        

main()
