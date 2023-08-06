import { ServerConnection } from '@jupyterlab/services';
import { URLExt } from '@jupyterlab/coreutils';
import { FetchHoc } from '@quetz-frontend/apputils';
import { withRouter } from 'react-router-dom';
import * as React from 'react';
import PackageVersions from './versions';
class PackageMainContent extends React.PureComponent {
    constructor() {
        super(...arguments);
        this._formatPlatform = (platforms) => {
            const linux = [];
            const osx = [];
            const win = [];
            const other = [];
            platforms.forEach((platform) => {
                const os = platform.split('-')[0];
                switch (os) {
                    case 'linux':
                        linux.push(platform);
                        break;
                    case 'osx':
                        osx.push(platform);
                        break;
                    case 'win':
                        win.push(platform);
                        break;
                    default:
                        other.push(platform);
                        break;
                }
            });
            if (other.length === 1 && other[0] === 'noarch') {
                return (React.createElement("div", { className: "package-platform-icons" },
                    React.createElement("i", { className: "fa fa-linux fa-2x package-platform-icon" }),
                    React.createElement("i", { className: "fa fa-apple fa-2x package-platform-icon" }),
                    React.createElement("i", { className: "fa fa-windows fa-2x package-platform-icon" })));
            }
            return (React.createElement("div", { className: "package-row-flex" },
                linux.length !== 0 && (React.createElement("div", null,
                    React.createElement("div", { className: "package-files-row" },
                        React.createElement("i", { className: "fa fa-linux fa-2x" })),
                    React.createElement("ul", { className: "package-platform-list" }, linux.map((platform, index) => (React.createElement("p", { key: index }, platform)))))),
                osx.length !== 0 && (React.createElement("div", null,
                    React.createElement("div", { className: "package-files-row" },
                        React.createElement("i", { className: "fa fa-apple fa-2x" })),
                    React.createElement("ul", { className: "package-platform-list" }, osx.map((platform, index) => (React.createElement("p", { key: index }, platform)))))),
                win.length !== 0 && (React.createElement("div", null,
                    React.createElement("div", { className: "package-files-row" },
                        React.createElement("i", { className: "fa fa-windows fa-2x" })),
                    React.createElement("ul", { className: "package-platform-list" }, win.map((platform, index) => (React.createElement("p", { key: index }, platform)))))),
                other.length !== 0 && (React.createElement("div", null,
                    React.createElement("ul", { className: "package-platform-list" }, other.map((platform, index) => (React.createElement("p", { key: index }, platform))))))));
        };
    }
    render() {
        const { match: { params: { packageId, channelId }, }, } = this.props;
        const settings = ServerConnection.makeSettings();
        const url = URLExt.join(settings.baseUrl, '/api/channels', channelId, '/packages', packageId);
        return (React.createElement("div", { className: "padding jp-table" },
            React.createElement(FetchHoc, { url: url, loadingMessage: "Fetching package information", genericErrorMessage: "Error fetching package information" }, (packageData) => (React.createElement(React.Fragment, null,
                React.createElement("h4", { className: "section-heading" }, "Summary"),
                React.createElement("p", { className: "minor-paragraph" }, packageData.summary || React.createElement("i", null, "n/a")),
                React.createElement("h4", { className: "section-heading" }, "Description"),
                React.createElement("p", { className: "minor-paragraph" }, packageData.description || React.createElement("i", null, "n/a")),
                packageData.platforms && packageData.platforms.lenght !== 0 && (React.createElement("div", null,
                    React.createElement("h4", { className: "section-heading" }, "Platforms"),
                    this._formatPlatform(packageData.platforms)))))),
            React.createElement(PackageVersions, { selectedPackage: packageId, channel: channelId })));
    }
}
export default withRouter(PackageMainContent);
//# sourceMappingURL=tab-info.js.map