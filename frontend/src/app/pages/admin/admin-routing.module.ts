
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from '../../pages/admin/dashboard/dashboard.component';
import { PasswordComponent } from './account/password/password.component';
import { ProfileComponent } from './account/profile/profile.component';
import { ListComponent as ListNotifiactionComponent } from './account/notification/list/list.component';
import { DetailComponent as DetailNotificationComponent } from './account/notification/detail/detail.component';
// CRUD Contact
import { DetailComponent as ContactDetailComponent } from './contact/detail/detail.component';
import { ListComponent as ContactListComponent } from './contact/list/list.component';
import { CreateComponent as ContactCreateComponent } from './contact/create/create.component';
import { EditComponent  as ContactEditComponent } from './contact/edit/edit.component';

const contactRoutes = [
  {
    path: '',
    component: ContactDetailComponent,
    children:[{ path: 'contact/detail/:id', component: ContactDetailComponent, data: { pageTitle: 'Contact' } }]
  },
  {
    path: '',
    component: ContactListComponent,
    children:[{ path: 'contact/list', component: ContactListComponent, data: { pageTitle: 'Contact' } }]
  },
  {
    path: '',
    component: ContactCreateComponent,
    children:[{ path: 'contact/create', component: ContactCreateComponent, data: { pageTitle: 'Contact' } }]
  },
  {
    path: '',
    component: ContactEditComponent,
    children:[{ path: 'contact/edit/:id', component: ContactEditComponent, data: { pageTitle: 'Contact' } }]
  }
]


const routes: Routes = [
  {
     path: '',
     component: DashboardComponent,
     children:[{ path: 'dashboard', component: DashboardComponent, data: { pageTitle: 'Dashboard' } }]
  },
  {
    path: '',
    component: ProfileComponent,
    children:[{ path: 'account/profile', component: ProfileComponent, data: { pageTitle: 'Profile' } }]
 },
 {
    path: '',
    component: PasswordComponent,
    children:[{ path: 'account/password', component: PasswordComponent, data: { pageTitle: 'Password' } }]
  },
  {
    path: '',
    component: ListNotifiactionComponent,
    children:[{ path: 'notification/list', component: ListNotifiactionComponent, data: { pageTitle: 'Notification' } }]
  },
  {
    path: '',
    component: DetailNotificationComponent,
    children:[{ path: 'notification/detail/:id', component: DetailNotificationComponent, data: { pageTitle: 'Notification' } }]
  },
  ...contactRoutes
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
