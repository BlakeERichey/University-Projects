delete from donation_drive
where donation_drive.title
not in
 (select donation_drive.title from donation_drive,donor_donations
  where donation_drive.title = donor_donations.donation_drive_title);
