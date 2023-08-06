import { ServerConnection } from '@jupyterlab/services';
import { URLExt } from '@jupyterlab/coreutils';
import { FetchHoc, formatSize } from '@quetz-frontend/apputils';
import { map } from 'lodash';
import fromNow from 'fromnow';
import * as React from 'react';
class PackageVersions extends React.PureComponent {
    render() {
        const { channel, selectedPackage } = this.props;
        const settings = ServerConnection.makeSettings();
        const url = URLExt.join(settings.baseUrl, '/api/channels', channel, '/packages', selectedPackage, '/versions');
        return (React.createElement(FetchHoc, { url: url, loadingMessage: `Loading versions in ${selectedPackage}`, genericErrorMessage: "Error fetching package versions information" }, (versionData) => {
            if (versionData.length === 0) {
                return React.createElement("div", null, "No versions available for the package");
            }
            const info = versionData[0].info;
            return (React.createElement(React.Fragment, null,
                React.createElement("div", { className: "package-row-flex" },
                    React.createElement("div", null,
                        React.createElement("h4", { className: "section-heading" }, "Package Info"),
                        React.createElement("p", { className: "minor-paragraph" },
                            React.createElement("b", null, "Arch"),
                            ": ",
                            info.arch || 'n/a',
                            React.createElement("br", null),
                            React.createElement("b", null, "Build"),
                            ": ",
                            info.build || 'n/a',
                            React.createElement("br", null),
                            React.createElement("b", null, "MD5"),
                            ": ",
                            info.md5,
                            React.createElement("br", null),
                            React.createElement("b", null, "Platform"),
                            ": ",
                            versionData[0].platform || info.platform,
                            React.createElement("br", null),
                            React.createElement("b", null, "Version"),
                            ": ",
                            info.version)),
                    React.createElement("div", null,
                        React.createElement("h4", { className: "section-heading" }, "Install"),
                        React.createElement("div", { className: "package-install-command" },
                            React.createElement("pre", null,
                                "mamba install -c ",
                                channel,
                                " ",
                                selectedPackage)))),
                React.createElement("h4", { className: "section-heading" }, "Dependencies"),
                React.createElement("p", { className: "minor-paragraph" }, map(info.depends, (dep, key) => (React.createElement("span", { key: key, className: "tag" }, dep)))),
                React.createElement("h4", { className: "section-heading" }, "History"),
                React.createElement("table", { className: "table-small full-width" },
                    React.createElement("thead", null,
                        React.createElement("tr", null,
                            React.createElement("th", null, "Uploader"),
                            React.createElement("th", null, "Date"),
                            React.createElement("th", null, "Filename"),
                            React.createElement("th", null, "Platform"),
                            React.createElement("th", null, "Size"),
                            React.createElement("th", null, "Version"))),
                    React.createElement("tbody", null, versionData.map((version) => (React.createElement("tr", { key: version.time_created },
                        React.createElement("td", null, version.uploader.name),
                        React.createElement("td", null, fromNow(version.time_created, {
                            max: 1,
                            suffix: true,
                        })),
                        React.createElement("td", null,
                            React.createElement("a", { href: URLExt.join(settings.baseUrl, `/get/${channel}/${version.info.subdir}/${version.filename}`), download: true }, version.filename)),
                        React.createElement("td", null, version.info.platform === 'linux' ? (React.createElement("i", { className: "fa fa-linux fa-2x" })) : version.info.platform === 'osx' ? (React.createElement("i", { className: "fa fa-apple fa-2x" })) : version.info.platform === 'win' ? (React.createElement("i", { className: "fa fa-windows fa-2x" })) : (React.createElement("div", { className: "package-platform-noarch" },
                            React.createElement("i", { className: "fa fa-linux" }),
                            React.createElement("i", { className: "fa fa-apple" }),
                            React.createElement("i", { className: "fa fa-windows" })))),
                        React.createElement("td", null, formatSize(version.info.size)),
                        React.createElement("td", null, version.version))))))));
        }));
    }
}
export default PackageVersions;
//# sourceMappingURL=versions.js.map