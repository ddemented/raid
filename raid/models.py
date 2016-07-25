from raid import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    Userid = db.Column(db.String(15), primary_key=True)
    UserName = db.Column(db.String(20))
    Pass = db.Column(db.String(20))
    UserRole = db.Column(db.String(20))
    FirstName = db.Column(db.String(25))
    MiddleName = db.Column(db.String(25))
    LastName = db.Column(db.String(25))
    Email1 = db.Column(db.String(50))
    Email2 = db.Column(db.String(50))
    Mobile1 = db.Column(db.String(15))
    Mobile2 = db.Column(db.String(15))
    AddressLine1 = db.Column(db.String(55))
    AddressLine2 = db.Column(db.String(55))
    City = db.Column(db.String(20))
    State = db.Column(db.String(20))
    Country = db.Column(db.String(15))
    Pincode = db.Column(db.String(7))
    CreationDate = db.Column(db.DateTime)
    CreatorId = db.Column(db.String(12))
    CafeId = db.Column(db.String(12))
    WalletId = db.Column(db.String(12))
    LastLoginDate = db.Column(db.DateTime)
    LastLoginCafe = db.Column(db.String(12))
    UniqueIdType = db.Column(db.String(15))
    UniqueIdNumber = db.Column(db.String(15))
    IsUserLoggedIn = db.Column(db.Integer)
    
    def __init__(self, userid, username, password, userrole, firstname, middlename, lastname, email1, email2, mobile1, mobile2, addline1, addline2, city, state, country, pincode, creatorid, cafeid, walletid, uniqueidtype, uniqueidnumber):
        self.Userid = userid
        self.UserName = username
        self.Pass = password
        self.UserRole = userrole
        self.FirstName = firstname
        self.MiddleName = middlename
        self.LastName = lastname
        self.Email1 = email1
        self.Email2 = email2
        self.Mobile1 = mobile1
        self.Mobile2 = mobile2
        self.AddressLine1 = addline1
        self.AddressLine2 = addline2
        self.City = city
        self.State = state
        self.Country = country
        self.Pincode = pincode
        self.CreationDate = datetime.now()
        self.CreatorID = creatorid
        self.CafeId = cafeid
        self.WalletId = walletid
        self.LastLoginDate = datetime.now()
        self.LastLoginCafe = None
        self.UniqueIdType = uniqueidtype
        self.UniqueIdNumber = uniqueidnumber
        self.IsUserLoggedIn = 0;