import { BaseSequelizeService, ISchema } from '../../../core/domain/services';
import { CivilStatus } from './civilStatus.model';

export class CivilStatusService extends BaseSequelizeService {
    protected define() {
        return {
            route: 'civil-statuses',
            model: CivilStatus
        };
    }

    protected defineCreateSchema(): ISchema {
        return {};
    }

    protected defineUpdateSchema(): ISchema {
        return {};
    }
}
