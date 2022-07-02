import { Component } from '@angular/core';
import { Router, Event, NavigationStart, NavigationEnd, NavigationError  } from '@angular/router';
import { Tooltip } from 'bootstrap'
import { ngxLoadingAnimationTypes } from 'ngx-loading';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  public loading:boolean = false;

  public loadingConfig = {
    backdropBorderRadius: '17px',
    fullScreenBackdrop: true,
    backdropBackgroundColour: '#dc3545',
    animationType: ngxLoadingAnimationTypes.chasingDots
  }


  constructor(private router: Router) {

      this.router.events.subscribe((event: Event) => {

        if (event instanceof NavigationStart) {
            // Show loading indicator
            this.setToolTip(event);
            this.loading = true;
        }

        if (event instanceof NavigationEnd) {
            // Hide loading indicator
            let app = this
            this.setToolTip(event);
            setTimeout(function(){



              let currentRoute = app.router.url
              if(document.getElementById("public-footer")){
                 if(currentRoute === '/account/password' || currentRoute === '/account/profile'){
                    document.getElementById("public-footer").classList.add("fixed-bottom");
                 }else{
                    document.getElementById("public-footer").classList.remove("fixed-bottom")
                 }
              }


              app.loading = false;
            }, 1500);
        }

        if (event instanceof NavigationError) {
            // Hide loading indicator

            // Present error to user
            this.setToolTip(event);
            this.loading = false;
        }
      });

  }

  setToolTip(event: any){


    let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new Tooltip(tooltipTriggerEl)
    })

    const tooltip = document.querySelector('.tooltip')
    if (tooltip !== null) document.body.removeChild(tooltip)

  }


}
