import stress from './DataView/stress' 
import history from './DataView/history' 
import temp from './DataView/temp'
import dash from './DataView/dash'
import line1 from './DataView/line1'
const components = {
  stress,
  history,
  temp,
  dash,
  line1,
};

const install = (Vue = {}) => {
  if (install.installed) return;
  Object.keys(components).forEach(component => {
    Vue.component(components[component].name, components[component]);
  });

  install.installed = true;
};

install.installed = false;

if (typeof window !== "undefined" && window.Vue) {
  install(window.Vue);
  install.installed = true;
}

