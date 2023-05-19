#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import argparse
import time
from datetime import datetime
import subprocess

# Provide your email credentials and the email details
sender_email = ''
## This is an app password so its probably okay to keep in plaintext
sender_password = ''

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Create a multipart message and set the headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Create a secure SSL context
        context = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        # Login to Gmail
        context.login(sender_email, sender_password)

        # Send the email
        context.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the connection
        context.quit()

        print('Email sent successfully!')
    except smtplib.SMTPAuthenticationError:
        print('Failed to authenticate with Gmail.')
    except smtplib.SMTPException as e:
        print('An error occurred while sending the email:', str(e))

def parse_args():
    parser = argparse.ArgumentParser(description='ARCANA Runner')
    parser.add_argument('program', type=str,
                    help='Program to run in quotes ""')
    parser.add_argument('--send-to', type=str,
                        default=getpass.getuser()+"@illinois.edu",
                        help='Email to send the program. Default picks from NETID')
    parser.add_argument("--subject", type=str,
                        help='Subject of email -- by default command and time')
    return parser.parse_args()

def main():
    args = parse_args()
    current_user = getpass.getuser()

    print("-----RUNNING PROGRAM-----")
    exec_start_clock = datetime.now().strftime('%H:%M:%S')
    exec_start_clock += " " + str(datetime.now().astimezone().tzinfo)
    start_time = time.time()

    result = subprocess.run(args.program, shell=True)
    end_time = round(time.time() - start_time, 5)
    print("-----------DONE----------")
    exec_finish_clock = datetime.now().strftime('%H:%M:%S')
    exec_finish_clock += " " + str(datetime.now().astimezone().tzinfo)

    curr_date = datetime.now().strftime('%d-%b-%y')

    subject = "[" + curr_date + "] Automated Execution Report "
    subject += "| App: " + args.program.split()[0]
    body = "Dear " + current_user + ",\n\n"
    body += "The report of the most recent run here:\n\n"

    run_body = "Return code: " + str(result.returncode) + "\n"
    run_body += "Execution started at: " + exec_start_clock + "\n"
    run_body += "Execution finished at: " + exec_finish_clock + "\n"
    run_body += "Execution time: " + str(end_time) + "(s)\n"
    run_body += "Full command: " + args.program + "\n"

    print("\n" + run_body)

    body += run_body
    body += "\nYour friendly neighbourhood,\nArcanaBot \u2764\uFE0F"

    send_email(sender_email, sender_password, args.send_to, subject, body)

if __name__ == '__main__':
    main()