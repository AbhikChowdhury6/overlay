import * as React from 'react';
import { TouchableOpacity, Image, Text, TextInput, View, StyleSheet } from 'react-native';
import {TabBarIOS, Mapview} from 'react-native';
//import indexStyle from './app.css';

// or any pure javascript modules available in npm
import {Slider, Keyboard} from 'react-native';

export default class MoodScreen extends React.Component {
  static navigationOptions = ({navigation}) => {
    return {
      headerTitle: 'Log Mood',
      headerRight: (
        <View/>
      ),
      headerLeft: (
        <TouchableOpacity onPress={() => navigation.openDrawer()}>
          <Image
            style={{width:40, height: 40}}
            source={require('./menu-512.png')}
          />
        </TouchableOpacity>
      )
    }
  }

  constructor(props){
    super(props);
    this.state = {text:''};
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style = {styles.mood}> MOOD</Text>
        <Slider style = {styles.sliderStyle}
          minimumValue = {0}
          maximumValue = {3}
          step = {1}
          />
        <View style = {styles.moodOptions}>
          <Text style = {styles.moods}>SAD</Text>
          <Text style = {styles.moods}>ANGRY</Text>
          <Text style = {styles.moods}>EXCITED</Text>
          <Text style = {styles.moods}>HAPPY</Text>
        </View>
        <Text style={styles.journalEntry}>Journal Entry</Text>
        <TextInput
        style ={styles.textinput}
        placeholder= 'How do you feel?'
        multiline = {true}
        onChangeText={(text)=>this.setState({text})}
        onSubmitEditing={Keyboard.dismiss}
        returnKeyType={"done"}

          />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: 15,
    backgroundColor: 'powderblue',
  },
  sliderStyle: {
    width: 315,
  },
  moodOptions: {
    flexDirection: 'row',
    justifyContent: 'center',
  },
  mood:{
    fontSize: 30,
  },
  moods:{
    margin:20,
    color: '#841584',
  },
  textinput: {
    borderWidth: 1,
    width: 300,
    height: 300,
    },
    journalEntry:{
      fontSize: 30,
      margin: 20,
    }

});
