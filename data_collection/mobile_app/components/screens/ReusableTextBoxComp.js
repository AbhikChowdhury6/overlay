import React, { Component } from 'react';
import { Text, View,TextInput, StyleSheet } from 'react-native';
import {AppRegistry, Image, LinearGradient, Button, Alert, TouchableOpacity } from 'react-native';

export default class ReusableTextBox extends Component{
constructor(props) {
  super(props);
}
//props.placeholder
render(){
    return(
      <View style = {styles.textButtonContainer}>
        <TextInput style = {styles.inputfields} placeholder = {this.props.placeholder}/>
        <View style = {styles.buttonStyle}>
        <Button
          onPress={this.props.onPress}
          title = "SEND"
          color="#841584"
          accessibilityLabel={this.props.accessibilityLabel}
        />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  textButtonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    padding: 20,
  },
  inputfields: {
    alignSelf: 'flex-start',
    height: 60,
    width: 200,
    fontSize: 20,
    borderWidth: 1,
    color: 'black',
    borderColor: '#FFFF',
    margin: 10,
  },
  buttonStyle: {
    justifyContent: 'center',
  }

});
