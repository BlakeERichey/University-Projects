Select donation_drive.title,donation_drive.theme,donation_drive.start_date,
donation_drive.end_date,sum(donor_donations.amount)
From
Donor_donations,donation_drive
where donor_donations.donation_drive_title = donation_drive.title
group by donation_drive.title,donation_drive.theme,donation_drive.start_date,
Donation_drive.end_date,donation_drive.goal
Having
sum(donor_donations.amount) >= donation_drive.goal;
