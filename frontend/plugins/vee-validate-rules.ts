import { defineRule, configure } from 'vee-validate';
import AllRules from '@vee-validate/rules';
export default defineNuxtPlugin(() => {
  configure({
    generateMessage: () => {
      return 'This field is required';
    },
  });

  
  Object.keys(AllRules).forEach(rule => {
    defineRule(rule, AllRules[rule]);
  });


});