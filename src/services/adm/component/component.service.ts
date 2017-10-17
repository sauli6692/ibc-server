import { BaseSequelizeService } from '../../../core/domain/services/BaseSequelizeService';
import { Component } from './component.model';

export class ComponentService extends BaseSequelizeService {
    protected define() {
        return {
            name: 'components',
            model: Component
        };
    }
}
