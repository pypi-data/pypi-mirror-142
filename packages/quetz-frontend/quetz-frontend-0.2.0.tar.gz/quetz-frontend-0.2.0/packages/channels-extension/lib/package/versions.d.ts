import { API_STATUSES } from '@quetz-frontend/apputils';
import * as React from 'react';
declare type PackageVersionProps = {
    channel: string;
    selectedPackage: string;
};
declare type PackageVersionsState = {
    versionData: null | any;
    apiStatus: API_STATUSES;
};
declare class PackageVersions extends React.PureComponent<PackageVersionProps, PackageVersionsState> {
    render(): JSX.Element;
}
export default PackageVersions;
