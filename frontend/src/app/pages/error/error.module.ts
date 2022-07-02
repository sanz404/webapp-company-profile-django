import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ErrorRoutingModule } from './error-routing.module';
import { Page404Component } from './page404/page404.component';
import { Page400Component } from './page400/page400.component';
import { Page401Component } from './page401/page401.component';
import { Page403Component } from './page403/page403.component';
import { Page500Component } from './page500/page500.component';
import { Page503Component } from './page503/page503.component';


@NgModule({
  declarations: [
    Page404Component,
    Page400Component,
    Page401Component,
    Page403Component,
    Page500Component,
    Page503Component
  ],
  imports: [
    CommonModule,
    ErrorRoutingModule
  ]
})
export class ErrorModule { }
