import React from 'react';
import { Text, View } from 'react-native';

const Header = (props) => {
  return (
    <View style={{
      alignItems: 'center',
      justifyContent: 'center',
      height: 60,
    }}>
      <Text>Overlay</Text>
    </View>
  );
}

export default Header;
