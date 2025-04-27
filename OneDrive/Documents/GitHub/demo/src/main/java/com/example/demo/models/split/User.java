package com.example.demo.models;

import lombok.Getter;
import lombok.Setter;


@Getter
@Setter
public class User {
    String userId;
    String userName;
    String emailId;
    Integer phoneNumber;
    Boolean isVerified;

    public User(String userId, String name, String emailId, Integer phoneNo, Boolean isVerified){
        this.userId = userId;
        this.userName = name;
        this.emailId = emailId;
        this.phoneNumber = phoneNo;
        this.isVerified = isVerified;
    }
}
