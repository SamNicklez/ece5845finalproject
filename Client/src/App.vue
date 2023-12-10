<template>
  <div class="main-div">
    <v-tabs v-model="tab" bg-color="primary" @click="reset">
      <v-tab value="one">Query 1 (PostgreSQL)</v-tab>
      <v-tab value="two">Query 2 (Neo4j)</v-tab>
      <v-tab value="three">Query 3 (IDK)</v-tab>
    </v-tabs>
    <div class="header-container">
      <v-window v-model="tab">
        <v-window-item value="one" class="query-one">
          <h1>Top 10 jobs based on a your inputted preferences</h1>
          <h2>Please select your preferred country</h2>
          <v-autocomplete v-model="selectedCountry" label="Input Country" :items="countries"
            @blur="submitCountry"></v-autocomplete>
          <h2 v-if="this.selectedCountry">Please select your preferred city</h2>
          <v-autocomplete v-model="selectedCity" v-if="this.selectedCountry" label="Input City" :items="cities"
            @blur="submitCity"></v-autocomplete>
          <h2 v-if="this.selectedCity">Please select your preferred sector</h2>
          <v-autocomplete v-model="selectedSector" v-if="this.selectedCity" label="Input City"
            :items="sectors"></v-autocomplete>
          <h2 v-if="this.selectedSector">Please rank these company traits (top being highest priority)</h2>
          <draggable v-if="this.selectedSector" class="draggable-container" :list="list" @change="log">
            <div class="draggable-text-container" v-for="element, index in list" :key="element.name">
              <p>{{ index + 1 }}. {{ element.name }}</p>
            </div>
          </draggable>
          <v-btn v-if="this.selectedSector" @click="calculatePostgreSQLQuery"
            style="margin-top: 2.5vh; margin-bottom: 5vh;" color="deep-purple-darken-2">Submit</v-btn>
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
      sectors: ["Technology", "Finance", "Healthcare"],
      dragging: false,
      returnData: null,
      selectedCountry: null,
      selectedCity: null,
      selectedSector: null,

    }
  },
  methods: {
    log(event) {
      console.log(event)
      console.log(this.list)
    },
    submitCountry() {
      console.log(this.selectedCountry)
      //Grab list of cities from backend and set to dropdown
    },
    submitCity() {
      console.log(this.selectedCity)
      //Grab list of cities from backend and set to dropdown
    },
    calculatePostgreSQLQuery() {
      console.log(this.selectedCountry)
      console.log(this.selectedCity)
      console.log(this.selectedSector)
      let preferences = this.list.map(item => item.id)
      console.log(preferences)
      //Grab list of cities from backend and set to dropdown
    },
    reset() {
      this.selectedCountry = null
      this.selectedCity = null
      this.selectedSector = null
      console.log("HIT")
    }
  },
  async created() {
    //Grab list of countries from backend and set to dropdown
    var requestOptions = {
      method: 'GET',
      redirect: 'follow',
      headers: {
        'Content-Type': 'application/json',
      }
    };

    fetch("http://127.0.0.1:5000/countries/distinct", requestOptions)
      .then(response => response.json()) // Assuming the response is in JSON format
      .then(result => {
        this.countries = result.map(country =>
          country.split(' ').map(word =>
            word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
          ).join(' ')
        );
      })
      .catch(error => console.log('error', error));

  },
})
</script>

<style>
.draggable-container {
  font-size: 1.5em;
  margin-bottom: 5vh;
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