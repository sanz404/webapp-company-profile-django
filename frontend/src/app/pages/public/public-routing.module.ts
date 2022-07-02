import { PortfolioDetailComponent } from './portfolio-detail/portfolio-detail.component';
import { BlogDetailComponent } from './blog-detail/blog-detail.component';
import { PortfolioComponent } from './portfolio/portfolio.component';
import { PricingComponent } from './pricing/pricing.component';
import { FaqComponent } from './faq/faq.component';
import { HomeComponent } from '../../pages/public/home/home.component';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { BlogComponent } from './blog/blog.component';
import { PasswordComponent } from './account/password/password.component';
import { ProfileComponent } from './account/profile/profile.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', component: HomeComponent, children:[{ path: 'home', component: HomeComponent, data: { pageTitle: 'Home' } }] },
  { path: '', component: AboutComponent, children:[{ path: 'about', component: AboutComponent, data: { pageTitle: 'About us' } }] },
  { path: '', component: ContactComponent, children:[{ path: 'contact', component: ContactComponent,  data: { pageTitle: 'Contact' } }] },
  { path: '', component: FaqComponent, children:[{ path: 'faq', component: ContactComponent,  data: { pageTitle: 'FAQ' } }] },
  { path: '', component: PricingComponent, children:[{ path: 'pricing', component: PricingComponent,  data: { pageTitle: 'Pricing' } }] },
  { path: '', component: PortfolioComponent, children:[{ path: 'portfolio', component: PortfolioComponent,  data: { pageTitle: 'Portfolio' } }] },
  { path: '', component: BlogComponent, children:[{ path: 'blog', component: BlogComponent,  data: { pageTitle: 'Blog' } }] },
  { path: '', component: BlogDetailComponent, children:[{ path: 'blog/:slug', component: BlogDetailComponent,  data: { pageTitle: 'Blog' } }] },
  { path: '', component: PortfolioDetailComponent, children:[{ path: 'portfolio/:slug', component: PortfolioDetailComponent,  data: { pageTitle: 'Portfolio' } }] },
  { path: '', component: PasswordComponent, children:[{ path: 'account/password', component: PasswordComponent, data: { pageTitle: 'Password' } }] },
  { path: '', component: ProfileComponent, children:[{ path: 'account/profile', component: ProfileComponent, data: { pageTitle: 'Profile' } }] },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PublicRoutingModule { }
