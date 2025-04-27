package com.example.demo.Manager;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.example.demo.Enums.SplitType;
import com.example.demo.models.Split;
import com.example.demo.models.expense.Expense;
import com.example.demo.models.split.ExpenseMetaData;
import com.example.demo.models.split.User;

public class SplitWiseManager {
    Map<String, User> userMap;
    Map<String, Map<String, Double>> balanceSheet;
    List<Expense> expenses;

    public SplitWiseManager(){
        this.userMap = new HashMap<>();
        this.expenses = new ArrayList<>();
        this.balanceSheet = new HashMap<>();
    }

    public void addUser(User user){
        userMap.put(user.getUserId(), user);
        balanceSheet.put(user.getUserId(), new HashMap<>());
    }

    public void addExpense(SplitType splitType, double amount, String userId, List<Split> splits, ExpenseMetaData expenseMetaData){
        Expense expense =  createExpense(splitType, amount, userMap.get(userId), splits, expenseMetaData);
    }

    private Expense createExpense(SplitType splitType, double amount, User user, List<Split> splits, ExpenseMetaData expenseMetaData) {
        for(Split split : splits){

        }
        throw new UnsupportedOperationException("Unimplemented method 'createExpense'");
    }
    private void updateBalanceSheetAfterExpenses(String paidBy, Expense expense){
        for(Split split : expense.getSplits()){
            String paidTo = split.getUser().getUserId();
            Map<String, Double> balances = balanceSheet.get(paidBy);
            if(!balances.containsKey(paidTo)){
                balances.put(paidTo, 0.0);
            }
            balances.put(paidTo,balances.get(paidTo) + split.getAmount());
            balances = balanceSheet.get(paidTo);   
        }
    }
}