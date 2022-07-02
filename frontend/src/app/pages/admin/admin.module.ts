import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ChartsModule } from 'ng2-charts';

import { AdminRoutingModule } from './admin-routing.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ProfileComponent } from './account/profile/profile.component';
import { PasswordComponent } from './account/password/password.component';
import { ListComponent } from './account/notification/list/list.component';
import { DetailComponent } from './account/notification/detail/detail.component';

// CRUD Contact
import { DetailComponent as ContactDetailComponent } from './contact/detail/detail.component';
import { ListComponent as ContactListComponent } from './contact/list/list.component';
import { CreateComponent as ContactCreateComponent } from './contact/create/create.component';
import { EditComponent  as ContactEditComponent } from './contact/edit/edit.component';
import { BarChartComponent } from './dashboard/bar-chart/bar-chart.component';
import { PieChartComponent } from './dashboard/pie-chart/pie-chart.component';




@NgModule({
  declarations: [
    DashboardComponent,
    ProfileComponent,
    PasswordComponent,
    ListComponent,
    DetailComponent,
    ContactListComponent,
    ContactDetailComponent,
    ContactCreateComponent,
    ContactEditComponent,
    BarChartComponent,
    PieChartComponent
  ],
  imports: [
    CommonModule,
    AdminRoutingModule,
    RouterModule,
    ChartsModule
  ]
})
export class AdminModule { }
