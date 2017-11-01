const Sequelize = require('sequelize');
import { BaseModel, IAssociation } from '../../../core/domain/models';

export class RoleComponent extends BaseModel {
	protected define() {
		return {
			name: 'RoleComponent',
			fields: {
				roleId: {
					type: Sequelize.INTEGER,
					primaryKey: true
				},
				componentId: {
                    type: Sequelize.INTEGER,
					primaryKey: true
				}
			}
		};
	}
}
