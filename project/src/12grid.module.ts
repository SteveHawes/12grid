import { NgModule } from '@angular/core';
import { CollapseDirective } from './collapse/collapse.directive';

@NgModule( {
    declarations: [CollapseDirective],
    exports: [CollapseDirective],
    imports: [],
    providers: []
} )
export class GridModule { }
