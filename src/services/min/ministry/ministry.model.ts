const Sequelize = require('sequelize');
import { BaseModel, IAssociation } from '../../../core/domain/models/';

export class Ministry extends BaseModel {
	protected define() {
		return {
			name: 'Ministry',
			fields: {
                id: {
					type: Sequelize.INTEGER,
					autoIncrement: true,
					primaryKey: true
				},
				name: {
					type: Sequelize.STRING(100),
					allowNull: false
				},
				description: {
					type: Sequelize.STRING(255),
					allowNull: true
				}
			}
		};
	}

    protected setAssociations(): IAssociation {
        return {
			oneToMany: [{
				model: 'MinistryObjective',
				as: 'objectives',
				foreignKey: 'ministryId',
                source: true
			}]
		};
    }
}
