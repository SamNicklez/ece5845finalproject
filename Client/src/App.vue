<template>
  <div class="main-div">
    <v-tabs v-model="tab" bg-color="primary">
      <v-tab value="one">Query 1 (PostgreSQL)</v-tab>
      <v-tab value="two">Query 2 (Neo4j)</v-tab>
      <v-tab value="three">Query 3 (IDK)</v-tab>
    </v-tabs>
    <div class="header-container">
      <v-window v-model="tab">
        <v-window-item value="one" class="query-one">
          <h1>Top 10 jobs based on a your inputted preferences</h1>
          <h2>Please select your preferred country</h2>
          <v-autocomplete v-model="selectedCountry" label="Input Country" :items="countries" @blur="test"></v-autocomplete>
          <h2 v-if="this.cities.length != 0" >Please select your preferred city</h2>
          <v-autocomplete v-model="selectedCity" v-if="this.cities.length != 0" label="Input City" :items="cities"></v-autocomplete>
          <h2>Please rank these company traits (top being highest priority)</h2>
          <draggable class="draggable-container" :list="list" @change="log">
            <div class="draggable-text-container" v-for="element,index in list" :key="element.name">
              <p>{{ index + 1  }}. {{ element.name }}</p>
            </div>
          </draggable>
          <v-btn @click="calculatePostgreSQLQuery">Submit</v-btn>
        </v-window-item>

        <v-window-item value="two">
          Two
        </v-window-item>

        <v-window-item value="three">
          Three
        </v-window-item>
      </v-window>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue'
import { VueDraggableNext } from 'vue-draggable-next'
export default defineComponent({
  components: {
    draggable: VueDraggableNext,
  },
  data() {
    return {
      tab: null,
      enabled: true,
      list: [
        { name: 'Potential Opportunities', id: 'opportunities_ranking' },
        { name: 'Compensation/Benefits', id: 'comp_benefits_ranking' },
        { name: 'Culture/Values', id: 'culture_values_ranking' },
        { name: 'Senior Management', id: 'senior_management_ranking' },
        { name: 'Worklife Balance', id: 'worklife_balance_ranking' },
        { name: 'CEO Approval', id: 'ceo_approval_ranking' },
        { name: 'Company Outlook', id: 'company_outlook_ranking' },
      ],
      countries: ["United States", "Mexico", "Canada"],
      cities: ["Iowa City"],
      dragging: false,
      returnData: null,
      selectedCountry: null,
      selectedCity: null,

    }
  },
  methods: {
    log(event) {
      console.log(event)
      console.log(this.list)
    },
    submitCountry(){
      console.log(this.selectedCountry)
      //Grab list of cities from backend and set to dropdown
    },
    calculatePostgreSQLQuery() {
      console.log(this.selectedCountry)
      console.log(this.selectedCity)
      let list = this.list.map(item => item.id)
      let data = {
        country: this.selectedCountry,
        city: this.selectedCity,
        list: list
      }
      //Grab list of cities from backend and set to dropdown
    },
  },
  async created() {
    //Grab list of countries from backend and set to dropdown
  },
})
</script>

<style>
.draggable-container {
  font-size: 2.5em;
}

.header-container {
  max-width: 60vw;
  outline: solid;
  margin: 2.5vh auto;
}

.draggable-text-container {
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
  cursor: move;
}

.main-div {
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: white;
}

h1 {
  font-size: 2em;
  padding: 1em;
}
h2 {
  font-size: 1.5em;
  margin-top: 5vh;
}
.query-one {
  padding: 1em;
}
</style>